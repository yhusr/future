# -*- coding:utf-8 -*-
# @Time    :2019/11/14 0014 8:53
# @Author  :toy_yh
# @File    :handle_requests.py
# @Software:PyCharm

import requests
import json


class HandleRequests:
    def __init__(self):
        self.one_session = requests.session()

    def common_heads(self, heads):
        self.one_session.headers.update(heads)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                data = eval(data)
                print(e)
        method = method.lower()
        if method == 'get':
            res = self.one_session.request(method, url, params=data, **kwargs)
        elif method in ('post', 'put', 'delete', 'patch'):
            """
          这个方式发送请求参数的传输方式以：data（form表单形式）或者json（application/json）形式，共两种方式
          """
            if is_json:
                res = self.one_session.request(method, url, json=data, **kwargs)
            else:
                res = self.one_session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print(f'此方法{method}不存在')

        return res

    def close(self):
        self.one_session.close()


if __name__ == '__main__':
    # 注册
    url = 'http://api.lemonban.com/futureloan/member/register'
    params = "{'mobile_phone' : '13900001003','pwd' : '12345678'}"
    heads = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    mr = HandleRequests()
    mr.common_heads(heads)
    res = mr.send(url, data=params)
