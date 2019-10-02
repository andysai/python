import random
# 从控制台选择要出的拳 - 石头(1) / 剪刀(2) / 布(3)
# 电脑随机出拳 - 先假定电脑只会出石头，完成整体代码功能
player = int(input("请输入您要出的拳 石头(1) / 剪刀(2) / 布(3) ："))
computer = random.randint(1,3)

def chooise(number) :
    if number == 1 :
        number = '石头'
        return number
    elif number == 2 :
        number = '剪刀'
        return number
    elif number == 3 :
        number = '布'
        return number
    else :
        print("请按照提示进行选择！！")

def judge(player,computer) :
    if chooise(player) == chooise(computer) :
        print("平局")
    elif chooise(player) == '石头' and chooise(computer) == '剪刀' :
        print("玩家获胜")
    elif chooise(computer) == '石头' and chooise(player) == '剪刀' :
        print("电脑获胜")
    elif chooise(player) == '石头' and chooise(computer) == '布':
        print("玩家获胜")
    elif chooise(computer) == '石头' and chooise(player) == '布':
        print("电脑获胜")
    elif chooise(player) == '剪刀' and chooise(computer) == '布':
        print("玩家获胜")
    elif chooise(computer) == '剪刀' and chooise(player) == '布':
        print("电脑获胜")

if __name__ == '__main__' :
    print("玩家出的是 %s - 电脑出的是 %s " % (chooise(player),chooise(computer)))
    judge(player, computer)