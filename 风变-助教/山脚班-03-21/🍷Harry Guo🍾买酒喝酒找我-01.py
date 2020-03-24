group = []
n = 0
while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    n = n + 1
    group.append([a + b])
    # 需要将每一对实验者的选择存起来。
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break

print('是第' + str(n) + '对实验者做出了最优选择')
# 打印是第几对实验者做出了最优选择。
for i in range(n):
    print('第' + str(i + 1) + '组的选择是' + str(group[i]))
# 通过循环打印每一对实验者的选择。