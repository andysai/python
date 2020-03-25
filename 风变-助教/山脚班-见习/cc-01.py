# 请你补充代码，让两位囚徒输入自己的选择，将其存成变量a,b
while True:
    a=input('囚徒1是否认罪')
    b=input('囚徒2是否认罪')
    if a=='认罪' and b=='认罪':
        print('判决')
        break
