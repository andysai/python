# 请你补充代码，让两位囚徒输入自己的选择，将其存成变量a,b
a = input("请输入认罪或者不认罪:")
b = input("请输入认罪或者不认罪:")
while True:
    if a == '认罪' and b == '认罪':
        print("都判10年")
        break
    elif a == '认罪' and b == '不认罪':
        print("1年 VS 20年")
        break
    elif a == '不认罪' and b == '认罪':
        print("20年 VS 1年")
        break
    else :
        print("都判3年")
        break
    break
    #避免死循环