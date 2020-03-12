class Spend():
    # 设置三个参数
    # subway是单程要坐10站，bus是坐公交的次数，taxi是搭乘出租车的里程
    def __init__(self, subway=10, bus=1, taxi=6.5):
        self.subway_spend = subway * 0.5  # 地铁出行费用
        self.bus_spend = bus * 2  # 公交出行费用
        self.taxi_spend = taxi * 4  # 出租车的出行费用

    def compare(self):
        print('坐地铁上班，单程要花%s元' % self.subway_spend)
        print('坐公交上班，单程要花%s元' % self.bus_spend)
        print('坐出租车上班，单程要花%s元' % self.taxi_spend)

    def price(self):
        if self.subway_spend < self.bus_spend and self.subway_spend < self.taxi_spend:
            print('地铁最省钱')
        elif self.subway_spend > self.bus_spend and self.subway_spend > self.taxi_spend:
            print('出租车最省钱')
        elif self.subway_spend > self.bus_spend and self.subway_spend < self.taxi_spend:
            print('公交最省钱')
a = Spend()

a.price()

