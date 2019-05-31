# coding:utf-8

from xlutils import copy
import xlrd,xlwt,re,os

# 创建表格
def cretaTable(self):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('sheet_1')
        workbook.save('E:\\H5_AutoTest\\Public_file\\book.xlsx')


# 向表格继续添加数据
def write(self,rows,value):
        excel_path='E:\\H5_AutoTest\\Public_file\\book.xlsx'
        rbook = xlrd.open_workbook(excel_path,formatting_info=True)
        wbook = copy.copy(rbook)
        w_sheet = wbook.get_sheet('sheet_1')
        r = rows
        c = 0
        values = value
        w_sheet.write(r,c,values)
        wbook.save(excel_path)


# 读取表格数据
def read(self,rows):
        wb = xlrd.open_workbook(u'E:\\H5_AutoTest\\Public_file\\book.xlsx','w+b')
        sheet1 = wb.sheet_by_name('sheet_1')
        r = int(rows)
        c = 0
        k1 = sheet1.cell(r,c)
        value = re.findall(r"'(.+?)'", str(k1))
        return value

# 清空数据
def wipe_excel(self):
        try:
                os.remove('E:\\H5_AutoTest\\Public_file\\book.xlsx')
                print('数据删除成功！')
        except:
                print('数据清理失败！')
        return wipe_excel(self)
