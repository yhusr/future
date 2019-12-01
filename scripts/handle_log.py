"""
Time:2019/11/6 0006
"""
import logging
import time
import os

from scripts.handle_conf import uy
from scripts.handle_path import LOGPATH


class HandleLog:

    @classmethod
    def get_logger(cls):
        f = uy.open_yaml('log', 'formate')
        formats = logging.Formatter(f)
        my_logger = logging.getLogger(uy.open_yaml('log', 'logname'))
        my_logger.setLevel(uy.open_yaml('log', 'level'))
        # 控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(uy.open_yaml('log', 'level'))
        sh.setFormatter(formats)
        my_logger.addHandler(sh)

        # 文件输出
        ts = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_path = os.path.join(LOGPATH, f'test_{ts}.log')
        fh = logging.FileHandler(log_path, encoding='utf8')
        fh.setLevel(uy.open_yaml('log', 'level'))
        fh.setFormatter(formats)
        my_logger.addHandler(fh)

        return my_logger


lt = HandleLog.get_logger()