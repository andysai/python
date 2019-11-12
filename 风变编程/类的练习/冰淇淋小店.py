# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让它继承9-1或9-4编写的Restaurant类。
# 这两个版本的Restaurant类都可以，选一个即可。
# 添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return '\n餐馆的名字为:' + self.restaurant_name + '\n菜肴有:' + self.cuisine_type

    def open_restaurant(self):
        return '餐馆正在营业'

