students = ['小明','小红','小刚']

for i in range(3):
    student = students[0]
    del students[0]
    students.append(student)
    print(students)
