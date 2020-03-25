students = ['小明','小红','小刚']

a = 0
while a < 3:
    student = students.pop(0)
    students.append(student)
    print(students)
    a = a + 1


