class B:
    name = 'alice'
    age = 18

class A(B):
    pass

member = A()
print(member.age)
print(member.name)