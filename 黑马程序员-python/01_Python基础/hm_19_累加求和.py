# 1.定义初始化次数
num = 0
# 2.定义结果变量
sum = 0
# 3.循环统计结果
while num <= 100 :
    sum = num + sum
    num += 1
print("0到100之间的数字求和结果 = %d" % sum)