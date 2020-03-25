def function1(month):
    if month<6:
        bonus=500
    elif 6<=month<=12:
        bonus=120*month
    else:
        bonus=180*month
    return bonus

def function2(name,month):
    print('该员工来了%d个月，获得奖金%d元' % (month,function1(month)))

function2('大聪',14)