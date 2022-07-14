N = int(input())

students = []
for _ in range(N):
    student = input().split()
    for i in range(1, 4):
        student[i] = int(student[i])
    students.append(student)

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
