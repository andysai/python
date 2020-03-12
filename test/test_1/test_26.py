while True:
    a = float(input("请输入a的值(不能小于0且不能大于100):"))
    b = float(input("请输入b的值(不能小于0且不能大于100):"))
    if a > 0 and b <= 100 :
        print('{} + {} = {}'.format(a,b,a+b))
    elif a < 0 and a > 100 :
        print('a的值请输入大于0或者小于100的数')
    elif b < 0 and b > 100:
        print('b的值请输入大于0或者小于100的数')
    elif a == 'q' or b == 'q':
        break
    elif a not in range(1,101) or b not in range(1,101) :
        print("请输入1到100之间的值")