i=24
while True:
    a=input('请您猜猜我的数:')
    if int(a)==i:
        print('猜对了')
        break
if a<24:
    print('太小了')
else:
    print('太大了')