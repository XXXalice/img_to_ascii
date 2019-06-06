from logging import Formatter, getLogger, StreamHandler, DEBUG, handlers
import math
import inspect

class Logger():
    def __init__(self, log_file, n=__name__,):
        const_abs_path = inspect.stack()[0][1]
        print(const_abs_path)
        self.logger = getLogger(n)
        self.logger.setLevel(DEBUG)
        formatt = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #stdout
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

        save_log_path = '/'+'/'.join(const_abs_path.split('/')[:-1])+'/'
        handler = handlers.RotatingFileHandler(
            filename=save_log_path + log_file,
            maxBytes=math.inf, # どのアルファベットで間違えたかの研究のため現状無制限にしてある
            backupCount=5
        )
        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg, errmsg):
        self.logger.error(msg + ' [{}]'.format(errmsg))

    def critical(self, msg):
        self.logger.critical(msg)

    def _trace_test(self):
        trace = inspect.stack()
        return trace[0]