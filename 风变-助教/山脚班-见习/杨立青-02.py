i=24
while a<3:
    guess=input('你来猜猜我心里想的数字是多少:')
    if int(guess)==i:
        print('猜对了')
        break
    elif int(guess)<i:
        print('太小了')
    else:
        print('太大了')
    a=a+1
    continue
else:
    print('失败了')