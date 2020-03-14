# 请补充下面的代码，添加4种判决和跳出语句，让代码满足练习要求。
while True:
    a = input('A，你认罪吗？请回答认罪或者不认')
    b = input('B，你认罪吗？请回答认罪或者不认')
    if a =='认罪'and b == '认罪':
        print('两人都得判10年，唉')
    elif a =='不认'and b =='认罪':
        print('A判20年，B判1年，唉')
    elif a =='认罪'and b == '不认':
        print('A判1年，B判20年')
    elif a =='认罪' and b == '不认':
        print('都判3年，太棒了')
        break
    else:
        print('别捣乱，只能回答“认罪”或“不认”！')