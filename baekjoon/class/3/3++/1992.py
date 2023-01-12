# 쿼드트리
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
answer = ""


def solve(x, y, n):
    global answer
    num = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != num:
                half = n // 2
                answer += "("
                solve(x, y, half)
                solve(x, y + half, half)
                solve(x + half, y, half)
                solve(x + half, y + half, half)
                answer += ")"
                return
    if num == 0:
        answer += "0"
    else:
        answer += "1"


solve(0, 0, N)

print(answer)

"""
- 난이도: 실버1
- 분류: 분할정복

- 최종결과까지 재귀적으로 생성해야 하는 문제.
"""
