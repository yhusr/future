"""
Time:2019/11/6 0006
"""
import openpyxl

from scripts.handle_path import EXCELPATH


class Sexcel:
    pass


class HandleExcel:
    def __init__(self, sheet_name, filepath=None):
        if filepath is None:
            self.filepath = EXCELPATH
        else:
            self.filepath = filepath
        self.sheet_name = sheet_name

    # 打开excel
    def open_excel(self):
        self.workbook = openpyxl.load_workbook(self.filepath)
        self.sheet = self.workbook[self.sheet_name]

    # 读取excel中的数据
    def read_excel(self):
        self.open_excel()
        row_li = list(self.sheet.rows)
        head_li = [h.value for h in row_li[0]]
        obj_li = []
        for i in row_li[1:]:
            se = Sexcel()
            value_li = [v.value for v in i]
            hv_zip = zip(head_li, value_li)
            for hv in hv_zip:
                setattr(se, hv[0], hv[1])
            obj_li.append(se)
        self.workbook.close()
        return obj_li

    # 写入内容到excel中
    def write_excel(self, row_num, col_num, val):
        self.open_excel()
        self.sheet.cell(row_num, col_num, val)
        self.workbook.save(self.filepath)
        self.workbook.close()
