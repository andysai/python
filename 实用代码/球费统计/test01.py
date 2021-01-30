# import time
import datetime
current_date = datetime.datetime.now()
# date = time.strftime('%Y-%m-%d', time.localtime())
# date1 = date.replace('-', '年')
#
#
month = str(current_date.month)
day = str(current_date.day)

date_now = month + "月" + day + "日"
print(date_now)

# 人均
# number_of_participants_list = []
# while True:
#     a = input("请输入参与人姓名:")
#     if a == 'q':
#         break
#     else:
#         number_of_participants_list.append(a)
#
# f = open('a.txt','w')
# for i in number_of_participants_list:
#     d = i + "/"
#     f.write(d)
# f.close()

# s = open('a.txt', 'r')
# num = s.readline()
# num1 = s.readline()
# print(num.replace("\n", ''))
# print('参与人数:', num1.replace("\n", ''))
# # for i in s.readlines():
# #     print(i.replace("\n", ''))
# s.close()


