# 배열 복원하기
H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]
A = [[0] * W for _ in range(H)]

# 일단 좌상단의 안겹치는 부분만 B에서 A로 복사.
for i in range(H):
    for j in range(W):
        if not (i >= X and j >= Y):
            A[i][j] = B[i][j]

# 겹치는 부분에서 A의 원래 값: 'B의 현재값 - 현재 칸에서 (X, Y) 뺀 좌표의 A값'
for i in range(H):
    for j in range(W):
        if i >= X and j >= Y:
            A[i][j] = B[i][j] - A[i - X][j - Y]

for row in A:
    print(*row)
