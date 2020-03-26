# 先补全代码，然后再运行。
# 可体会多重继承中的就近原则。
class Teacher:
    face = 'serious'
    job = 'teacher'

class Father:
    face = 'sweet'
    parenthood = 'dad'

class A1(Teacher, Father):
    face='gertle'


class A2(A1):
    pass


time3 = A1()

print(time3.face)