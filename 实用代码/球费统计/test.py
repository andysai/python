# 导入模块
import xlrd
import xlwt

# 创建工作簿
workbook = xlwt.Workbook()
# 创建工作表
worksheet = workbook.add_sheet("test")

# 设置样式
def style_1():
    # 初始化样式
    style = xlwt.XFStyle()
    # 创建字体属性
    font = xlwt.Font()
    # 对属性的值进行初始化
    font.name = "宋体"
    font.height = 20 * 20
    font.size = 14
    font.bold = True
    font.escapement = xlwt.Font.ESCAPEMENT_NONE

    # 创建边界属性
    borders = xlwt.Borders()
    # 对属性的值进行初始化
    borders.top = 1
    borders.bottom = 1
    borders.left = 1
    borders.right = 1

    # 创建对其属性
    alignment = xlwt.Alignment()
    # 对属性的值进行初始化
    alignment.vert = xlwt.Alignment.VERT_CENTER
    alignment.horz = xlwt.Alignment.HORZ_CENTER

    # 创建模式属性
    pattern = xlwt.Pattern()
    # 对属性的值进行初始化
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 24

    # 调用字体风格样式
    return style


style1 = style_1()


# 设置行高
# worksheet1.col(0).height_mismatch = True
# worksheet1.row(0).height = 20*40

# 数据整理
a = 0
Summary = ['时间','活动开销明细','支出','人均']
for i in Summary:
    worksheet.write(1,a,i)
    a += 1

# 合并单元格设置标题
# worksheet1.write_merge(0,0,0,3,"收支明细表",style1)
worksheet.write(2,3,"test",style1)
# 保存excle
workbook.save("test.xls")