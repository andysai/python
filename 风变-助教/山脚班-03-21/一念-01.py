#古灵阁欢迎辞
print("您好，欢迎来到古灵阁，请问您需要帮助吗？")
select = int(input(['1 需要','2 不需要']))
if select == 1:
    select1 = int(input("请问您需要提供什么帮助呢？['1 存取款','2 货币兑换','3 咨询']"))
    if select1 == 1:
        print("推荐你去存取窗口")
    elif select == 2:
        number=float(input("金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币"))
        if number=='N':
            print("好的，我知道了，您需要兑换"+str(number*51.3)+"人民币")
    elif select == 3:
        print("推荐你去咨询窗口。")
 elif select == 2:
    print("好的，再见.")