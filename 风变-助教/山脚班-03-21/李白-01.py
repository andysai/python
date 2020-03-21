choose = int(input('欢迎来到农业银行,请问是否需要帮助?[1需要,2不需要]'))
if choose == 1:
    choose1 = int(input('请问您需要办理什么业务?[1 咨询,2 兑换,3 存取款]'))
    if choose1 == 1:
        print('请前往柜台咨询')
    elif choose1 == 2:
        number = float(input('今天的美元与人民币的汇率是1:6.25,请问您兑换多少美元?'))
        if number >= 1:
            print('您需要给我' + str(number * 6.25) + '人民币')
            end = int(input('请将钱放入兑换仓，放置完毕请按[1]'))
            end1 = int(input('请收好您的金钱，请问是否还需要兑换美元?[1 是,2 否]'))

        while end1 == 1:
            number = float(input('今天的美元与人民币的汇率是1:6.25,请问您兑换多少美元?'))
            print('您需要给我' + str(number * 6.25) + '人民币')
            end = int(input('请将钱放入兑换仓，放置完毕请按[1]'))
            end1 = int(input('请收好您的金钱，请问是否还需要兑换美元?[1 是,2 否]'))
            if end1 == 2:
                print('谢谢光临,再见!')
    else:
        print('请前往自助存取款机')

else:
    print('谢谢光临,再见!')