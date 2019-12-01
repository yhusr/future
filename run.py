# -*- coding:utf-8 -*-
# @Time    :2019/11/15 0015 12:51
# @Author  :toy_yh
# @File    :run.py
# @Software:PyCharm
import unittest
import os
import time
from HTMLTestRunnerNew import HTMLTestRunner

from scripts.handle_conf import uy
from scripts.handle_path import REPORTSPATH,PERSONPATH,CASESPATH
from scripts.handle_phone import HandlePhone


class RunTests:

    @staticmethod
    def test_run():
        if not os.path.exists(PERSONPATH):
            HandlePhone.generate_register_phone()
        suit = unittest.defaultTestLoader.discover(CASESPATH)
        report_path = os.path.join(REPORTSPATH, uy.open_yaml('runcase', 'report') +
                                   time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) +
                                   '.html')
        runner = HTMLTestRunner(stream=open(report_path, 'wb'),
                                title=uy.open_yaml('runcase', 'title'),
                                description=uy.open_yaml('runcase', 'description'),
                                tester=uy.open_yaml('runcase', 'tester'))
        runner.run(suit)


if __name__ == '__main__':
    RunTests.test_run()
