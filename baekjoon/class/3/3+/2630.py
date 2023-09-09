# 색종이 만들기
# 출처: https://zidarn87.tistory.com/378
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0


def solve(x, y, n):
    global white, blue
    color = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 핵심: 시작한 좌표와 다른 값이 나오는 순간 4분할로 재귀
            if board[i][j] != color:
                half_n = n // 2
                solve(x, y, half_n)
                solve(x, y + half_n, half_n)
                solve(x + half_n, y, half_n)
                solve(x + half_n, y + half_n, half_n)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


solve(0, 0, N)

print(white)
print(blue)

"""
- 난이도: 실버2
- 풀이법은 똑같지만 구현이 훨씬 간단하다.
"""
