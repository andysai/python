class Student(object):
    def __init__(self, name, sex, tel):
        # 姓名、性别、手机号
        self.name = name
        self.sex = sex
        self.tel = tel

    def __str__(self):
        return f'姓名:{self.name}\n性别:{self.sex}\n手机号:{self.tel}'

# if __name__ == '__main__':
#     aa = Student('aa', '女', '11')
#     print(aa)