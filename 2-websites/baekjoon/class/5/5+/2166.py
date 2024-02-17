# 다각형의 면적
# 출처: https://shineild-security.tistory.com/164
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.append(arr[0])
x = 0
y = 0

# 공식 사용
for i in range(N):
    x += arr[i][0] * arr[i + 1][1]
    y += arr[i][1] * arr[i + 1][0]
answer = abs(round((x - y) / 2, 1))

print(answer)

"""
- 난이도: 골드5
- 분류: 기하
"""
