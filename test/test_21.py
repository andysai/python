panda_list = {'1号': '100', '2号': '86', '3号': '130', '4号': '140', '5号': '52','6号': '99'}
overweight = []

for num,weight in panda_list.items():
    if int(weight) > 110:
        overweight.append(num)
print(overweight)