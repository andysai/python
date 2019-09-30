# 定义两个整数变量 python_score、c_score 编写代码判断成绩
python_score = input("请输入python成绩：")
c_score = input("请输入c成绩：")

# 要求只要有一门成绩 > 60分就算及格
if python_score > '60' or c_score > '60' :
    print("及格")
else :
    print("不及格")