trusteeship =[]
f = open('trusteeship.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    trusteeship.append(list)
f.close()

for i in trusteeship:
    if i != '正常' and i != '关机' and i != '空闲':
        print(i)