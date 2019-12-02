# 导入模块
import xlrd
# 打开文档
wb = xlrd.open_workbook(r'E:\20191202.xlsx')
# 获取工作簿
print(wb.sheet_names())

table = wb.sheet_by_index(0)
# 获取行数
print(table.nrows)
# 获取列数
print(table.ncols)
#获取一行的值
print(table.row_values(1))
# 获取一列的值
print(table.col_values(1))
# 获取某个单元格的值
print(table.cell(0,0).value)
print(table.cell(1,1).value)