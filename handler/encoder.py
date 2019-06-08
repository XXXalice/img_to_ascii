import os
import sys
import inspect
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
        img = Image.open(BytesIO(bin))
        if collecting:
            try:
                fname, ext = fpath.split('/')[-1].split('.')
            except Exception as e:
                self.log.error('cant get files.', errmsg=e)
            save_file = os.path.join(self.strage_path, fname) + '.{}'.format(ext)
            img.save(save_file, quality=95)
        print(img.size)