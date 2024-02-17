# BOJ 10825
# 성적만 다시 숫자로 변경: 데이터를 한번씩 더 돌아야 해서 비효율적
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
