# 배열 돌리기 1
# 출처: https://resilient-923.tistory.com/303
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i  # 시작점: 좌상단
        val = arr[x][y]

        for j in range(i + 1, N - i):  # 좌
            x = j
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

        for j in range(i + 1, M - i):  # 하
            y = j
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

        for j in range(i + 1, N - i):  # 우
            x = N - j - 1
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

        for j in range(i + 1, M - i):  # 상
            y = M - j - 1
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

for row in arr:
    print(*row)

"""
- 더 깔끔한 풀이
"""
