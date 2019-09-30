# 1.定义一个整数变量 age ，编写代码判断年龄是否正确
# 要求人的年龄在0 - 120之间
age = int(input("请输入年龄："))
# 方法一：
# if 0 <= age <= 120 :
#     print("年龄正确")
# else :
#     print("年龄错误")
# 方法二：
if age >= 0 and age <= 120 :
    print("年龄正确")
else :
    print("年龄错误")