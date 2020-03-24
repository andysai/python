def div(num1, num2):
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + '%'
    return percent


def warning():
    print('error:你确定上个月一毛钱都不赚不亏嘛？')


def main():
    while true:
        num1 = float(input('请输入本月所获利润'))
        num2 = float(input('请输入上月所获利润'))
        if num2 == 0:
            warning()
        else:
            print('本月增长率：' + div(num1, num2))
            break


main()