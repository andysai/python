# 1.定义holiday_name 字符串变量记录节日名称
holiday_name = input('请输入节日名称(情人节/平安夜/生日)：')
# 2.如果是情人节 应该 买玫瑰/看电影
if holiday_name == '情人节' :
    print("买玫瑰")
    print("看电影")
# 3.如果是平安夜 应该 买苹果/吃大餐
elif holiday_name == '平安夜' :
    print("买苹果")
    print("吃大餐")
# 4.如果是生日 应该 买蛋糕
elif holiday_name == '生日' :
    print("买蛋糕")
# 5.其他的日子每天都是节日啊......
else :
    print("每天都是节日啊！！！")