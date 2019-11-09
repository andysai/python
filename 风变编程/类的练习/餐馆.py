# 9-1 餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项消息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，在调用前述的两个方法。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return '\n餐馆的名字为:' + self.restaurant_name + '\n菜肴有:' + self.cuisine_type

    def open_restaurant(self):
        return '餐馆正在营业'

restaurant = Restaurant('sai','番茄炒鸡蛋')
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

# 9-2 三家餐馆：根据9-1编写的类创建三个实例，并对每个实例调用方法describe_restaurant()
restaurant1 = Restaurant('andy','鸡蛋牛肉面')
print(restaurant1.describe_restaurant())
restaurant2 = Restaurant('king','烧鸭饭')
print(restaurant2.describe_restaurant())
restaurant3 = Restaurant('sss','蜜汁叉烧烤肉饭')
print(restaurant3.describe_restaurant())