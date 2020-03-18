def div(num1, num2):
    a = str((num2-num1)*100/num1) + '%'
    return a
def warning():
        print('Error: 你确定上个月一毛钱都不赚不亏吗？')
def main():
    month1 = float(input('请输入上月所获利润:'))
    month2 = float(input('请输入本月所获利润:'))
    if month1 == 0:
        warning()
    else:
        print('本月的利润增长率：' + div(month1,month2))
main()
