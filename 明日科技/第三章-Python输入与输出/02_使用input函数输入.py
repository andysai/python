#_*_ coding:utf-8 _*_
#开发人员：34431
#开发时间：2020-02-21 22:50
#文件名称:02_使用input函数输入.py
#开发工具：PyCharm

tip = input("请输入文字:")
print(tip)
print(type(tip))

height = float(input("请输入您的身高(单位:米):"))
weight = float(input("请输入您的体重(单位:千克):"))
# 计算BMI指数
bmi = weight / (height*height)

print("您的身高:{}\n您的体重:{}\n您的BMI指数:{}".format(height,weight,bmi))