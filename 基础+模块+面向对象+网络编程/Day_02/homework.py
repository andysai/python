#1、使用while循环输入 1 2 3 4 5 6 8 9 10
# mun = 1
# while mun <= 10 :
#     if mun == 7 :
#         pass
#     else:
#         print(mun)
#     mun += 1

#2、输出 1-100 内的所有奇数
# for i in range(1,101,2):
#     print(i)

#3、求1-2+3-4+5 ... 99的所有数的和
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum = sum + count
#     else:
#         sum = sum - count
#     count += 1
# print(sum)

#4、用户登陆(三次机会重试)
times = 1
while times <= 3:
    name = input("Please input your name :")
    passswd = input("Please input your password :")
    if name == 'sai' and passswd == '123456':
        print("登陆成功")
        break
    else:
        print("账号密码错误，请重新输入")
        print("你已经%d次输入错误" % (times))
    times += 1
