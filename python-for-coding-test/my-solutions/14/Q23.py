# BOJ 10825
N = int(input())

students = []
for _ in range(N):
    students.append(input().split())

# 문자로 저장된 성적을 숫자로 변환해서 비교
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
