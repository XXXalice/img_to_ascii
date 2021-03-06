import os
from .encoder import Encoder
import cv2
import numpy as np
import time
import curses
from PIL import Image

class MovieEncoder(Encoder):
    def __init__(self, fps):
        super().__init__()
        self.fps = fps

    def show_movie(self, fpath):
        movie_path = os.path.join(self.strage_path, fpath)
        try:
            cap = cv2.VideoCapture(movie_path)
            while(cap.isOpened()):
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame', gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            self.log.error(msg="can't init video file.", errmsg=str(e))
            return None
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def frame_capture(self, fpath):
        """
        動画のフレームを取得
        :param fpath: 動画のパス
        :return: frame一覧list（numpy.ndarray）
        """
        movie_path = os.path.join(self.strage_path, fpath)
        self.fname = fpath.split(".")[0]
        frames = []
        try:
            cap = cv2.VideoCapture(movie_path)
            while(cap.isOpened()):
                _, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frames.append(gray)
        except Exception as e:
            self.log.error(msg="can't init video file.", errmsg=str(e))
            return None
        finally:
            cap.release()
            cv2.destroyAllWindows()
            return frames

    def frame_split(self):
        """
        fpsに応じてフレームを減らす
        :return: 処理済みフレームリスト
        """
        pass

    def preprocess_frame(self, frames, aa_width=50):
        """
        フレーム一覧を受け取りaaに加工する
        :return: 処理済みフレーム
        """
        effects = "resize_gray"
        self.preprocessed_frames = []
        for frame in frames:
            pilimg = Image.fromarray(frame)
            preprocessed_frame = self.preprocess(effects, specify_img=pilimg, aa_width=aa_width)
            self.preprocessed_frames.append(preprocessed_frame)
        return self.preprocessed_frames

    def animation(self, frames, reverse_mode=False):
        self.__play_aa(stdscr=curses.initscr(), frames=frames, reverse_mode=reverse_mode)

    def __play_aa(self, stdscr, frames, reverse_mode=False):
        """
        cursesでアニメーションを実行する
        todo:
            フレームの短期的な保存方法の模索
            img_2_cchar()をそのまま利用する場合毎回.umeumeファイルとしてsaveが入るため処理が遅くなる

        """
        try:
            for frame in frames:
                char_frame = self.img_2_cchar(img=frame, reverse_mode=reverse_mode)
                print(char_frame)
                stdscr.clear()
                stdscr.addstr("aaa")
                time.sleep(0.3)
                stdscr.refresh()
        except Exception as e:
            exit(1)
        finally:
            curses.endwin()
