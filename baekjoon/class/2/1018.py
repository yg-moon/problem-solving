# 체스판 다시 칠하기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

min_cnt = int(1e9)
wb = list("WBWBWBWB")
bw = list("BWBWBWBW")

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        for type1, type2 in [[wb, bw], [bw, wb]]:
            cnt = 0
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    if x % 2 == 0:
                        if board[x][y] != type1[y - j]:
                            cnt += 1
                    else:
                        if board[x][y] != type2[y - j]:
                            cnt += 1
            min_cnt = min(min_cnt, cnt)

print(min_cnt)

"""
- 난이도: 실버4
- 분류: 브루트포스

구현
- (i,j)를 좌상단 시작점으로 잡고 8x8 범위까지 탐색.
- 좌상단 시작점이 W인 경우와 B인 경우를 나누어 완전탐색.
"""
