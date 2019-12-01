"""
Time:2019/11/6 0006
"""
import unittest
from libs.ddt import ddt, data

from scripts.handle_excel import HandleExcel
from scripts.handle_log import lt
from scripts.handle_conf import uy
from scripts.handle_mysql import HandleMysql
from scripts.handle_re import HandleRe
from scripts.handle_requests import HandleRequests


@ddt
class TestRegister(unittest.TestCase):
    eo = HandleExcel('register')
    cases = eo.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.hm = HandleMysql()
        cls.hr = HandleRequests()
        cls.hr.common_heads({'X-Lemonban-Media-Type': 'lemonban.v2'})

    @data(*cases)
    def test_excel_case(self, obj):
        title = obj.title
        base_url = uy.open_yaml('api', 'load')
        register_url = ''.join((base_url, obj.url))
        data_num = HandleRe.str_regex(obj.data)
        res = self.hr.send(url=register_url, data=data_num)
        res_data = res.json()
        code = res_data.get('code')
        msg = res_data.get('msg')
        expected_data = obj.expected
        msg_data = obj.msg
        try:
            # 多条信息进行断言
            self.assertListEqual([code, msg], [expected_data, msg_data], msg=f'用例{title}已执行')
        except AssertionError as e:
            self.eo.write_excel(int(obj.caseId) + 1, uy.open_yaml('excel', 'result_col'),
                                uy.open_yaml('excel', 'failed'))
            self.eo.write_excel(int(obj.caseId) + 1, uy.open_yaml('excel', 'response_col'), res.text)
            lt.error(e)
            raise e
        else:
            self.eo.write_excel(int(obj.caseId) + 1, uy.open_yaml('excel', 'result_col'),
                                uy.open_yaml('excel', 'expected'))
            self.eo.write_excel(int(obj.caseId) + 1, uy.open_yaml('excel', 'response_col'), res.text)
            lt.info(title)

    @classmethod
    def tearDownClass(cls):
        cls.hm.close()
        cls.hr.close()



