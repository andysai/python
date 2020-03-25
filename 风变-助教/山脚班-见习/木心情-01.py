b='三根皮带，四斤大豆'
def my_len(words):
#函数的参数是字符串
    a=0
    for i in words:
        a=a+1
    return a

print(my_len(b))
print(len(b))