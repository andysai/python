def div(num1, num2):
    growth = (num1 - num2) / num2
    prcent = str(growth * 100) + '%'
    return prcent


def warning():
    print('你确定一月份一毛钱也没赚没赔吗？')


def main():
    num1 = float(input('清输入二月份的利润'))
    num2 = float(input('请输入一月份的利润'))
    if num2 == 0:
        warning()
    else:
        print('本月利润增长率为' + div(num1, num2))


main()
