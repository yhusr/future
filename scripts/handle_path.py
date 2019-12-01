"""
Time:2019/11/17 0017
"""
import os

# 获取根目录路径
BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取配置文件目录
CONFIGPATH = os.path.join(BASEPATH, 'configs')

# 获取配置文件的具体路径
YAMLPATH = os.path.join(CONFIGPATH, 'casesconf.yaml')

# 获取excel的data路径
DATAPATH = os.path.join(BASEPATH, 'datas')

# 获取excel的具体路径
EXCELPATH = os.path.join(DATAPATH, 'excelcases.xlsx')

# 获取logs的目录路径
LOGPATH = os.path.join(BASEPATH, 'logs')

# 获取reports的目录路径
REPORTSPATH = os.path.join(BASEPATH, 'reports')

# 获取三种身份人员的信息的yaml存放路径
PERSONPATH = os.path.join(CONFIGPATH, 'register_phone.yaml')

# 获取用例类的路径
CASESPATH = os.path.join(BASEPATH, 'cases')

#获取token路径
TOKENPATH = os.path.join(CONFIGPATH,'token_infor.yaml')

pass
