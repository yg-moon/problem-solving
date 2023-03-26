# 세로읽기
arr = [[""] * 15 for _ in range(5)]

for i in range(5):
    s = input()
    for j, c in enumerate(s):
        arr[i][j] = c

answer = ""
for j in range(15):
    for i in range(5):
        answer += arr[i][j]
print(answer)

"""
- 난이도: 브론즈1
- 분류: 2차원 배열 (구현)

- 5x15 2차원 배열을 선언해서 푼다.
"""
