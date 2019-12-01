# -*- coding:utf-8 -*-
# @Time    :2019/11/22 0022 10:58
# @Author  :toy_yh
# @File    :handle_phone.py
# @Software:PyCharm
import os

from scripts.handle_requests import HandleRequests
from scripts.handle_conf import uy
from scripts.handle_mysql import HandleMysql
from scripts.handle_path import PERSONPATH
from scripts.handle_conf import HandleYaml


class HandlePhone:
    @staticmethod
    def send_phone_requests(username, type_num, password='12345678'):
        hr = HandleRequests()
        hm = HandleMysql()
        # 设置requests的头部
        hr.common_heads(uy.open_yaml('api', 'header'))
        # 设置url
        register_url = ''.join((uy.open_yaml('api', 'load'), uy.open_yaml('api', 'register')))

        # 如果mysql中未插入该条注册的数据，需要多次发送请求
        while True:
            phone_num = hm.get_my_phone()
            data = {
                "mobile_phone": phone_num,
                "pwd": password,
                "type": type_num,
                "reg_name": username
            }
            res_register = hr.send(register_url, data=data)
            # 获取响应中用户的手机号
            if res_register:
                user_id = hm.get_mysql_result(uy.open_yaml('mysql', 'phone_sql'), phone_num)[0]['id']
                break

        user_data = {username: {
            "userId": user_id,
            "userPhone": phone_num,
            "password": password,
            "regName": username
        }}

        hr.close()
        hm.close()

        return user_data

    @classmethod
    def generate_register_phone(cls):
        hy = HandleYaml(PERSONPATH)
        admin_requests = cls.send_phone_requests('admin',0)
        borrow_requests = cls.send_phone_requests('borrower',1)
        invest_requests = cls.send_phone_requests('investor',1)
        user_json = {}
        user_json.update(invest_requests)
        user_json.update(borrow_requests)
        user_json.update(admin_requests)
        hy.write_yaml(user_json,mode='w')


if __name__ == '__main__':
    HandlePhone.generate_register_phone()



