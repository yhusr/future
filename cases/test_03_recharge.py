"""
Time:2019/11/6 0006
"""
import unittest

from libs.ddt import ddt, data

from scripts.handle_excel import HandleExcel
from scripts.handle_log import lt
from scripts.handle_conf import uy,HandleYaml
from scripts.handle_mysql import HandleMysql
from scripts.handle_re import HandleRe
from scripts.handle_requests import HandleRequests
from scripts.handle_path import PERSONPATH
from scripts.handle_phone import HandlePhone


@ddt
class TestRecharge(unittest.TestCase):
    eo = HandleExcel('recharge')
    cases = eo.read_excel()
    hy = HandleYaml(PERSONPATH)

    @classmethod
    def setUpClass(cls):
        cls.hm = HandleMysql()
        cls.hr = HandleRequests()
        cls.hr.common_heads({'X-Lemonban-Media-Type': 'lemonban.v2'})

    @data(*cases)
    def test_excel_case(self, obj):
        #充值前生成手机号码以及相关成员的信息
        if obj.caseId == 1:
            HandlePhone.generate_register_phone()
        # 构造url
        register_url = ''.join((uy.open_yaml('api', 'load'), obj.url))
        # 获取请求参数
        data_num = HandleRe.str_regex(obj.data)
        # 数据库中查询数据的sql语句
        recharge_sql = obj.sql
        recharge_before = 0
        telephone = self.hy.open_yaml('investor', 'userPhone')
        if recharge_sql:
            tele_sql = self.hm.get_mysql_result(recharge_sql, args=[str(telephone)], is_more=False)
            if tele_sql['amount']:
                recharge_before = float(tele_sql['amount'])
        # Authorization
        # 发起请求
        res = self.hr.send(url=register_url, data=data_num)
        # 相应内容转换为json格式
        res_data = res.json()
        if obj.caseId == 2:
            self.hr.one_session.headers.update({'Authorization':'Bearer ' + res_data['data']['token_info']['token']})

        try:
            # 多条信息进行断言
            self.assertListEqual([res_data.get('code'), res_data.get('msg')], [obj.expected, obj.msg], msg=f'用例{obj.title}已执行')
            if recharge_sql:
                after_sql = self.hm.get_mysql_result(recharge_sql, args=[str(telephone)], is_more=False)
                recharge_after = float(after_sql['amount'])
                recharge_data = round((recharge_after - recharge_before), 2)
                expect_data = float(eval(obj.data)['amount'])
                self.assertEqual(recharge_data, expect_data)

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
            lt.info(obj.title)

    @classmethod
    def tearDownClass(cls):
        cls.hm.close()
        cls.hr.close()

if __name__ == '__main__':
    unittest.main()


