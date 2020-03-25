def math(month):
    global money
    if month < 6:
        money = '500'
    elif 6 <= month <= 12:
        money = month * 120
    else:
        money = month * 180
    return money


def match(n, month):
    m = math(month)
    print('该员工' + n + '来了' + str(m) + '个月，获得奖金' + str(money) + '元')


match('大聪', 14)