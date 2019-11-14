import os
from .encoder import Encoder
import cv2

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

