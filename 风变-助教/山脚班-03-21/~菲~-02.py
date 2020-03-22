a=24
for i in range(3):
    a=int(input('你猜我想的数字是多少,你只有三次机会:'))
    if a==24:
        print('猜对了')
        break
    elif a>24:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('三次机会你都答错了')