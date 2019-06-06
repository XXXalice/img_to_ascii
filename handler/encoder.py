import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + './handler/')
from .logger import Logger

class Encoder:
    def __init__(self):
        self.log = Logger('.aalog')