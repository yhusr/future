"""
Time:2019/11/6 0006
"""
import unittest
import json

from libs.ddt import ddt, data

from scripts.handle_excel import HandleExcel
from scripts.handle_log import lt
from scripts.handle_conf import uy
from scripts.handle_mysql import HandleMysql
from scripts.handle_re import HandleRe
from scripts.handle_requests import HandleRequests


@ddt
class TestAdd(unittest.TestCase):
    eo = HandleExcel('verify')
    cases = eo.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.hm = HandleMysql()
        cls.hr = HandleRequests()
        cls.hr.common_heads({'X-Lemonban-Media-Type': 'lemonban.v2'})

    @data(*cases)
    def test_excel_case(self, obj):
        # 构造url
        register_url = ''.join((uy.open_yaml('api', 'load'), obj.url))
        # 获取请求参数
        data_num = HandleRe.str_regex(obj.data)
        # Authorization
        # 发起请求
        res = self.hr.send(url=register_url, method=obj.method, data=data_num)
        res_data = res.json()
        if obj.caseId == 1:
            self.hr.one_session.headers.update({'Authorization': 'Bearer ' + res_data['data']['token_info']['token']})
        try:
            # 多条信息进行断言
            self.assertListEqual([res_data['code'], res_data['msg']], [obj.expected, obj.msg], msg=f'用例{obj.title}已执行')
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
            if obj.caseId == 2:
                setattr(HandleRe, 'get_loan_id', json.loads(data_num)['loan_id'])
                getattr(HandleRe, 'get_loan_id')
            lt.info(obj.title)

    @classmethod
    def tearDownClass(cls):
        cls.hm.close()
        cls.hr.close()

if __name__ == '__main__':
    unittest.main()


