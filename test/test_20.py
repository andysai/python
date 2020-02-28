a = [1,2,3]
b = a.append(4)
# print(b)

a = 0
#if a:
#    print(123)

dic = {'卡西':100,'严峻':97,'正义':99,'七七':96}
#dic.append('manman':100)
#print(dic)

#while 100>101:
#    print('while False')

#while 100<101:
#    print('while True')

#while False:
#    print('while False')

#if True:
#    print('while True')

a = 7
b = 8
#print('%d,%d' % (b,a))

num = 0
#while num < 100:
#    num += 1
#    if num % 2 == 0:
#        continue
#    print(num)


data = [{'陈奕迅': ['岁月如歌', '富士山下', '无条件'],
 '张敬轩':['我的天', '酷爱', '余震'],
 '杨千嬅':['野孩子', '少女的祈祷', '寒舍']},['小龙女', '杨过', '郭芙蓉'], ['东邪西毒', '东成西就', '阿飞正传', '花样年华', '2046'],
{'李安': '少年派的奇幻漂流', '诺兰': '盗梦空间', '陈凯歌': '霸王别姬'}]

#print(data[3]['陈凯歌'])


def name():
    b = '延君'
    name()
#print('%s喜欢冲浪和攀岩。' %b)

class People:
    def a(self):
        print('人生来就是要不断学习')
class Teacher(People):
    def a(self):
        print('老师的职责就是带领学生好好学习')
class Student(People):
    def a(self):
        print('学生的职责就是好好学习')
xiaoming = Student()
xiaoming.a()

class teacher():
    name = '延君'
    def work(self):
        print('learning ~~~')
t = teacher()
print(t.name)
t.work()











