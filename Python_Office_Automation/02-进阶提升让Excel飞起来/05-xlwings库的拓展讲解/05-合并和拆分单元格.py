"""


"""
# 导入模块
import xlwings as xw

# 创建实例
app = xw.App(visible=True, add_book=False)

# 打开工作簿
workbook = app.books.open("../source_material/03/2019年某公司员工薪资表.xlsx")

# 打开工作表
worksheet = workbook.sheets['sheet1']

# 获取方格区域
fg = worksheet.range("B1:H6")



