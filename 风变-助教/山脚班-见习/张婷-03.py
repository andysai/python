def egg():
    global quantity,quantity1,quantity2
    # 口红品牌
    quantity = 'Christain Louboutin'
    quantity1 = 'TomFord'
    quantity2 = 'Dior'

    return quantity,quantity1,quantity2

# 查看所有的口红信息
print(egg())

# 查找对应的口红
egg()
print(quantity)
print(quantity1)
print(quantity2)