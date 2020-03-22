students = ['小明','小红','小刚']
i = 0
while i < 3:
    student = students.pop(0)
    students.append(student)
    print(students)
    i += 1