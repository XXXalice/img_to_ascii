import os
import sys
import inspect
import gc
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + './handler/')
from .logger import Logger
from PIL import Image
from io import BytesIO

class Encoder:
    def __init__(self):
        self.log = Logger('.aalog')
        STRAGE_NAME = 'strage'
        self.strage_path = os.path.join('/'.join(inspect.stack()[0][1].split('/')[:-2]), STRAGE_NAME)

    def upload(self, fpath, collecting=True):
        with open(fpath, 'rb') as f:
            print(fpath)
            bin = f.read()
        self.img = Image.open(BytesIO(bin))
        if collecting:
            try:
                self.fname, ext = fpath.split('/')[-1].split('.')
            except Exception as e:
                self.log.error('cant get files.', errmsg=e)
            save_file = os.path.join(self.strage_path, self.fname) + '.{}'.format(ext)
            self.img.save(save_file, quality=95)
            self.log.info('saved img. {}'.format(str(save_file)))
        return self.img

    def preprocess(self, *effects, specify_img=None, aa_width=50):
        if specify_img is not None:
            processed_img = specify_img
            self.log.info('Using specify_img.')
        else:
            processed_img = self.img
        def_size = processed_img.size
        reduce_per = aa_width / def_size[0]
        EFFECT_DIC = {
            'resize': processed_img.resize((aa_width, int(def_size[1]*reduce_per))),
            'gray': processed_img.convert('L'),
            'resize_gray':processed_img.resize((aa_width, int(def_size[1]*reduce_per))).convert('L')
        }
        for ef in effects:
            try:
                processed_img = EFFECT_DIC[ef]
                self.log.info('Processed, [{}]'.format(ef))
            except:
                self.log.warn('Not implemented, [{}].'.format(ef))
                continue
        return processed_img

    def img_2_cchar(self, img=None, reverse_mode=False):
        if img is None:
            target_img = self.img
        else:
            target_img = img
        make_dic_iter = range(256) if reverse_mode else reversed(range(256))
        os.makedirs(os.path.join(self.strage_path, 'ascii'), exist_ok=True)
        x, y = target_img.size
        pixels = np.array(img.getdata()).reshape(y, x, -1)
        # pixels : 横（len==50）
        # つまり50が37個（縦）ある
        if not hasattr(self, 'cchars_dic'):
            with open(os.path.join(self.strage_path, 'cchar_dic.umeume'), 'r') as dic:
                cchars = [cchar.rstrip('\n') for cchar in dic.readlines()]
                self.cchars_dic = {idx: cchar for idx, cchar in zip(make_dic_iter, cchars)}
                # self.cchars_dic = {idx: cchar for idx, cchar in zip(reversed(range(256)), cchars)}
        cchar_art = ''

        for row in pixels:
            for col in row:
                cchar_art += self.cchars_dic[col[0]]
            cchar_art += '\n'
        self.__save(cchar_art)
        return cchar_art

    def __save(self, cchar_art):
        with open(os.path.join(self.strage_path, 'ascii', self.fname + '.umeume'), 'w') as f:
            f.write(cchar_art)
        self.log.info('Completed!')

    def __ram_reduction(self, *objs):
        for obj in objs:
            try:
                del obj
            except:
                self.log.warn('Could not delete {}'.format(str(obj)))
                continue
        gc.collect()
        self.log.info('Memory was released.')
