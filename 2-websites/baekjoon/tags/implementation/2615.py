# 오목
board = [list(map(int, input().split())) for _ in range(19)]

# 우, 하, 우하, 우상
# 단순 상하좌우가 아닐경우 이렇게 묶기
dir = [(0, 1), (1, 0), (1, 1), (-1, 1)]


def check(x, y, color):
    for dx, dy in dir:
        cnt = 1
        for k in range(1, 5):
            nx = x + k * dx  # 해당 방향으로 k칸 만큼 이동
            ny = y + k * dy
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                cnt += 1
            else:
                break
        if cnt == 5:
            if not (
                0 <= x - dx < 19 and 0 <= y - dy < 19 and board[x - dx][y - dy] == color
            ) and not (
                0 <= x + 5 * dx < 19
                and 0 <= y + 5 * dy < 19
                and board[x + 5 * dx][y + 5 * dy] == color
            ):
                return [color, x + 1, y + 1]
    return [-1, -1, -1]  # base case


def main():
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                result, pos_x, pos_y = check(i, j, board[i][j])
                if result != -1:
                    print(result)
                    print(pos_x, pos_y)
                    return
    print(0)  # 승부가 나지 않은 경우


main()

"""
- 난이도: 실버1
- 분류: 구현, 브루트포스

풀이
- 모든 지점에서 시작하여 가로, 세로, 대각 5개 확인

디버깅
- 1. 틀렸습니다
    - 이유: 우상단 대각선을 고려하지 않았음
- 2. 틀렸습니다
    - 이유: 6개 확인시 반대방향을 고려하지 않았음
"""
