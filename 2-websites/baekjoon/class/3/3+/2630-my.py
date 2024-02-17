# 색종이 만들기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0


def div_and_conq(x, y, n):
    global white, blue
    all_white = True
    all_blue = True
    # 핵심1: 시작위치를 기준으로 n만큼 탐색
    for i in range(x, x + n):  # 주의: 시작위치는 (0,0)이 아니라 (x,y)
        for j in range(y, y + n):
            if graph[i][j] == 1:
                all_white = False
            elif graph[i][j] == 0:
                all_blue = False
    if all_white:
        white += 1
    elif all_blue:
        blue += 1
    else:
        # 핵심2: 다음 시작위치를 n//2 만큼 떨어진 곳으로 설정하고 재귀
        for dx, dy in [(0, 0), (n // 2, 0), (0, n // 2), (n // 2, n // 2)]:
            nx = x + dx
            ny = y + dy
            div_and_conq(nx, ny, n // 2)


div_and_conq(0, 0, N)

print(white)
print(blue)

"""
- 난이도: 실버2
- 분류: 분할정복

- (정답을 보니 더 간단하게 구현할 수 있다.)
"""
