# 打印九九乘法表

# 1.定义1个计数器变量
i = 1

# 开始循环
while i <= 9 :
    # 定义一个计数器变量
    j = 1
    while j <= i :
        print("%d*%d=%d" % (i,j,(i*j)),end="\t")
        j += 1
    print("")
    i += 1

#for i in range(1,10):
#    for j in range(1,i+1):
#        print("%d*%d=%d" % (j,i,(i*j)),end=" ")
#        j += i
#    print("")
#    i += 1