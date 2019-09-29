Wages = int(input("请输入每月的工资："))
Credit_card = int(input("请输入每月的信用卡还款金额："))
Surplus = Wages - Credit_card
Quesion = input("今天发工资吗? (发/不发)" )
if Quesion == '发' :
    print("先还信用卡")
    if Surplus > 0 :
        print("又可以happy了,0(n_n)哈哈~")
    else :
        print("哦，no。。。还的等30天")
elif Quesion == '不发' :
    print("盼着工资")
else :
    print("请按要求输入相应的内容！")