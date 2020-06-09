a = '88f8.7217.bdd4'
# 先将.转换成-
a = a.replace('.','-')
#print(a)

# 将数据转换成列表
str_1=list(a)
print(len(str_1))
# 切换到需要转换的字符
nPos=str_1.index(a[2])
str_1.insert(nPos,'-')

nPos=str_1.index(a[7])
str_1.insert(nPos,'-')


str_2="".join(str_1)

# 输出
print(str_2)
print(len(str_2))
