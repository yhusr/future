# -*- coding:utf-8 -*-
# @Time    :2019/11/15 0015 9:24
# @Author  :toy_yh
# @File    :handle_mysql.py
# @Software:PyCharm

import pymysql
import random
from scripts.handle_conf import uy


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host=uy.open_yaml('mysql', 'host'),
                                    user=uy.open_yaml('mysql', 'user'),
                                    password=uy.open_yaml('mysql', 'password'),
                                    port=uy.open_yaml('mysql', 'port'),
                                    db=uy.open_yaml('mysql', 'db'),
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    @staticmethod
    def get_mobile():
        """
        随机获取手机号码
        :return:
        """
        return uy.open_yaml('mobile', 'phone') + ''.join(random.sample('0123456789', 8))

    def phone_is_exist(self, phone_num):
        """
        判断手机号码是否存在于数据库，返回相应的布尔值
        :param phone_num:
        :return:
        """
        sql_phone = uy.open_yaml('mysql', 'sql')
        my_result = self.get_mysql_result(sql_phone, args=phone_num, is_more=False)
        if my_result:
            return True
        else:
            return False

    def get_mysql_result(self, sql, args=None, is_more=True):
        """
        获取从mysql中获取的数据结果
        :param params: 传入的sql中的参数
        :param sql: 传入的sql语句
        :return:
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            mysql_result = self.cursor.fetchall()
        else:
            mysql_result = self.cursor.fetchone()
        return mysql_result

    def get_my_phone(self):
        """
        获取数据库不存在的并且是随机生成的号码
        :return:
        """
        phone_num = self.get_mobile()
        while True:
            if not self.phone_is_exist(phone_num):
                break
        return phone_num

    def close(self):
        """
        按照顺序关闭
        :return:
        """
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    mo = HandleMysql()
    # sql1 = "select * from member where mobile_phone=%s"
    # my_result = mo.get_mysql_result(sql1,args=['13900050004'],is_more=False)
    # print(my_result)
    print(mo.get_my_phone(),type(mo.get_my_phone()))
    mo.close()
