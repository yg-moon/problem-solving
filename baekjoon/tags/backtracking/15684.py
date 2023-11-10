# 사다리 조작
N, M, H = map(int, input().split())
board = [[False] * (N + 1) for _ in range(H + 1)]
answer = int(1e9)

# 핵심1: 표현방식을 결정
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = True


# i번 세로선의 결과가 i번인지 확인
def check_result():
    # 세로선 하나를 잡고 출발
    for i in range(1, N + 1):
        cur_col = i
        # 한칸씩 내려가면서 확인
        for cur_row in range(1, H + 1):
            # 오른쪽으로 이동
            if board[cur_row][cur_col]:
                cur_col += 1
            # 왼쪽으로 이동
            elif cur_col - 1 >= 1 and board[cur_row][cur_col - 1]:
                cur_col -= 1
        if cur_col != i:
            return False
    return True


# 현재 가로선을 추가할 수 있는지 확인
def is_possible(row, col):
    # 자신이 중복인지 확인
    if board[row][col]:
        return False
    # 서로 접하면 안 됨
    if board[row][col + 1] or (col - 1 >= 1 and board[row][col - 1]):
        return False
    return True


# 가능한 모든 가로선의 조합을 최대 3개까지 추가
def dfs(depth, cur_row, cur_col):
    global answer

    if check_result():
        answer = min(answer, depth)
        return

    # 핵심2: 조기종료 조건 및 위치
    if depth >= answer or depth == 3:
        return

    # 핵심3: 중복탐색 방지를 위해 시작지점을 잘 설정 (2차원 백트래킹)
    for row in range(cur_row, H + 1):
        col_start = cur_col if row == cur_row else 1
        for col in range(col_start, N):
            if is_possible(row, col):
                board[row][col] = True
                dfs(depth + 1, row, col)
                board[row][col] = False


dfs(0, 1, 1)

if answer <= 3:
    print(answer)
else:
    print(-1)

"""
- 난이도: 골드3
- 분류: 백트래킹

디버깅
- 문제: 시간초과
- 이유
    기본적인 것
    - 1. 조합을 찾을때 시작점을 제대로 지정하지 않아서 중복탐색을 했음
    - 2. 조기종료를 하지 않았음
    유의할 점
    - 3. 자료구조가 너무 무거웠음 (최대한 배열로 풀 것... 실행시간이 3배 차이남)
    - 4. 조기종료의 조건이 안 좋았음 (조합 탐색을 한단계 더하게 되어, 실행시간이 2배 이상 차이났음)
"""
