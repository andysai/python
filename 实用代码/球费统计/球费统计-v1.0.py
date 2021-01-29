# 导入模块
import xlwings as xw
import datetime

# 创建实例
app = xw.App(visible=True, add_book=False)

# 新建工作簿
workbook = app.books.add()

# 新建工作表
sheet1 = workbook.sheets.add("明细")
sheet2 = workbook.sheets.add("球费汇总")

# 获取日期
current_date = datetime.datetime.now()
year = str(current_date.year)
month = str(current_date.month)
day = str(current_date.day - 1)
date_now = year + "年" + month + "月" + day + "日"

# 填写数据
sht2_value = ['时间', '活动开销明细', '支出', '人均']
sheet2.range("A2:D2").value = sht2_value

# 日期
sheet2.range("A3").value = date_now

# 活动开销明细

# 支出
# 统计使用的羽毛球数量
badminton_free = int(input("请输入羽毛球的单价:"))
badminton_num = int(input("请输入使用的羽毛球数量:"))
f = open('a.txt', 'w')
f.write(f'羽毛球:{badminton_num}' + "\n")
f.close()
# 算出金额
sum_free = badminton_free * badminton_num
sheet2.range("C3").value = sum_free
# 人均
number_of_participants_list = []
while True:
    number_of_participants = input("请输入参与人姓名:")
    if number_of_participants == 'q':
        break
    else:
        number_of_participants_list.append(number_of_participants)

f = open('a.txt', 'a')
for i in number_of_participants_list:
    d = i + "/"
    f.write(d)
f.close()

s = open('a.txt', 'r')
num = s.readline()
num1 = s.readline()
message = num + '参与人数:' + num1
s.close()

sheet2.range("B3").value = message

per_capita = round(sum_free / len(number_of_participants_list))

sheet2.range("D3").value = per_capita
# 保存工作表
workbook.save('test.xlsx')

# 关闭工作表
workbook.close()
# 关闭工作簿
app.quit()