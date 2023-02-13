# 색종이
arr = [[0] * 100 for _ in range(100)]

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            answer += 1
print(answer)

"""
- 난이도: 실버5
- 분류: 구현

- 배운점
    - 이렇게 그래프에 직접 표시하면 쉽게 풀 수 있다.
    - 좌표 정보를 통해 겹치는 부분을 빼는 방식으로 풀었으면 훨씬 복잡했을 것이다.
"""
