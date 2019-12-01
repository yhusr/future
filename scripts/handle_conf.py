"""
Time:2019/11/6 0006
"""
import configparser
import yaml

from scripts.handle_path import YAMLPATH


class HandleConfig:
    def __init__(self, filepath):
        self.filepath = filepath
        self.conf = configparser.ConfigParser()

    def read_conf(self, section_name, option_name):
        self.conf.read(self.filepath, encoding='utf8')
        sc = self.conf.get(section_name, option_name)
        try:
            rc = eval(sc)
        except NameError as n:
            return sc
        else:
            return rc

    def write_conf(self, datas):
        for data in datas:
            self.conf[data] = datas[data]
        with open(self.filepath, 'a', encoding='utf8') as f:
            self.conf.write(f)


uc = HandleConfig(YAMLPATH)


class HandleYaml:
    def __init__(self, filepath):
        self.filepath = filepath

    def open_yaml(self, section_name, option_name):
        with open(self.filepath, encoding='utf8') as m:
            data = yaml.full_load(m)
        d = data[section_name][option_name]
        return d

    def write_yaml(self, datas,mode='a'):
        with open(self.filepath,mode, encoding='utf8') as y:
            yaml.dump(datas, y, allow_unicode=True)


uy = HandleYaml(YAMLPATH)
