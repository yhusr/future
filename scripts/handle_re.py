# -*- coding:utf-8 -*-
# @Time    :2019/11/20 0020 8:33
# @Author  :toy_yh
# @File    :handle_re.py
# @Software:PyCharm

import re

from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import HandleYaml
from scripts.handle_path import PERSONPATH,YAMLPATH


class HandleRe:
    @staticmethod
    def str_regex(strdata):
        """
        正则表达式替换内容
        :param strdata:
        :return:
        """

        if re.search(r'{no_exist_phone}', strdata):
            hm = HandleMysql()
            phone = hm.get_my_phone()
            res_data = re.sub(r'{no_exist_phone}', phone, strdata)
            hm.close()
            return res_data

        uy = HandleYaml(PERSONPATH)
        if re.search(r'{invest_phone}', strdata):
            user_phone = uy.open_yaml("investor", "userPhone")
            res_data = re.sub(r'{invest_phone}', user_phone, strdata)
            return res_data

        if re.search(r'{borrow_phone}', strdata):
            user_phone = uy.open_yaml("borrower", "userPhone")
            res_data = re.sub(r'{borrow_phone}', user_phone, strdata)
            return res_data

        if re.search(r'{user_id_re}', strdata):
            user_Id = str(uy.open_yaml("investor", "userId"))
            res_data = re.sub(r'{user_id_re}', user_Id, strdata)
            return res_data

        # {member_id_re}
        if re.search(r'{member_id_re}', strdata):
            user_Id = str(uy.open_yaml("borrower", "userId"))
            res_data = re.sub(r'{member_id_re}', user_Id, strdata)
            return res_data

        # {no_exist_num}
        if re.search(r'{no_exist_num}', strdata):
            hm = HandleMysql()
            loan_id = int(hm.get_mysql_result(uy.open_yaml('mysql', 'id_sql'))[0]['member_id'])+1
            res_data = re.sub(r'{no_exist_num}', str(loan_id), strdata)
            hm.close()
            return res_data

        #{loan_id_re}
        if re.search(r'{loan_id_re}', strdata):
            hm = HandleMysql()
            invent_id = uy.open_yaml('investor', 'userId')
            res_data = re.sub(r'{loan_id_re}', getattr(HandleRe, 'get_loan_id'), strdata)
            loan_data = re.sub(r'{user_id}', str(invent_id), res_data)
            hm.close()
            return loan_data

        # {admin_phone}
        if re.search(r'{admin_phone}', strdata):
            admin_phone = str(uy.open_yaml("admin", "userPhone"))
            res_data = re.sub(r'{admin_phone}', admin_phone, strdata)
            return res_data

        #{load_id}
        if re.search(r'{load_id}', strdata):
            hm = HandleMysql()
            hy = HandleYaml(YAMLPATH)
            borrow_id = uy.open_yaml('borrower', 'userId')
            member_id = hm.get_mysql_result(hy.open_yaml('mysql','loan_sql'), borrow_id)[0]['id']
            res_data = re.sub(r'{load_id}', str(member_id), strdata)
            hm.close()
            return res_data

        return strdata

if __name__ == '__main__':
    # phone_num = "{'mobile_phone':{no_exist_phone},'pwd':'12345678','type':1,'reg_name':'yh'}"
    # print(HandleRe.str_regex(phone_num))
    he = HandleRe()
    print(getattr(HandleRe,'get_loan_id'))

