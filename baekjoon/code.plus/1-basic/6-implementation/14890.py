# 경사로
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 각 행에 대해
for i in range(N):
    possible = True
    cur_num = board[i][0]
    slope = [0] * N  # 경사로의 위치
    for j in range(1, N):
        # 2 이상 차이나면 바로 중지
        if abs(cur_num - board[i][j]) >= 2:
            possible = False
            break
        # 더 큰게 나올 경우
        elif cur_num - board[i][j] == -1:
            tmp_cnt = 0
            tmp_j = j - 1
            tmp_slope = []
            while (
                0 <= i < N
                and 0 <= tmp_j < N
                and board[i][tmp_j] == cur_num
                and slope[tmp_j] != 1
                and tmp_cnt < L
            ):
                tmp_slope.append(tmp_j)
                tmp_cnt += 1
                tmp_j -= 1
            if tmp_cnt == L:
                # 경사로 위치 업데이트
                for ts in tmp_slope:
                    slope[ts] = 1
            else:
                possible = False
                break
        # 더 작은게 나올 경우
        elif cur_num - board[i][j] == 1:
            tmp_cnt = 0
            tmp_j = j  # 주의: 여기는 j+1 아님
            tmp_slope = []
            while (
                0 <= i < N
                and 0 <= tmp_j < N
                and board[i][tmp_j] == cur_num - 1
                and slope[tmp_j] != 1
                and tmp_cnt < L
            ):
                tmp_slope.append(tmp_j)
                tmp_cnt += 1
                tmp_j += 1
            if tmp_cnt == L:
                # 경사로 위치 업데이트
                for ts in tmp_slope:
                    slope[ts] = 1
            else:
                possible = False
                break
        cur_num = board[i][j]
    # 가능한 경로가 있으면 정답 + 1
    if possible:
        answer += 1

# 각 열에 대해
for j in range(N):
    possible = True
    cur_num = board[0][j]
    slope = [0] * N  # 경사로의 위치
    for i in range(1, N):
        # 2 이상 차이나면 바로 중지
        if abs(cur_num - board[i][j]) >= 2:
            possible = False
            break
        # 더 큰게 나올 경우
        elif cur_num - board[i][j] == -1:
            tmp_cnt = 0
            tmp_i = i - 1
            tmp_slope = []
            while (
                0 <= tmp_i < N
                and 0 <= j < N
                and board[tmp_i][j] == cur_num
                and slope[tmp_i] != 1
                and tmp_cnt < L
            ):
                tmp_slope.append(tmp_i)
                tmp_cnt += 1
                tmp_i -= 1
            if tmp_cnt == L:
                # 경사로 위치 업데이트
                for ts in tmp_slope:
                    slope[ts] = 1
            else:
                possible = False
                break
        # 더 작은게 나올 경우
        elif cur_num - board[i][j] == 1:
            tmp_cnt = 0
            tmp_i = i  # 주의: 여기는 i+1 아님
            tmp_slope = []
            while (
                0 <= tmp_i < N
                and 0 <= j < N
                and board[tmp_i][j] == cur_num - 1
                and slope[tmp_i] != 1
                and tmp_cnt < L
            ):
                tmp_slope.append(tmp_i)
                tmp_cnt += 1
                tmp_i += 1
            if tmp_cnt == L:
                # 경사로 위치 업데이트
                for ts in tmp_slope:
                    slope[ts] = 1
            else:
                possible = False
                break
        cur_num = board[i][j]
    # 가능한 경로가 있으면 정답 + 1
    if possible:
        answer += 1

print(answer)

"""
- 요약: 모든 경로를 다 한번씩 확인
- 구현
    - 각 행에 대해
        1. 맨 왼쪽에서 시작한다.
        2. 최근 숫자를 기억하면서 오른쪽으로 한칸씩 이동.
            - 2 이상 차이나면 현재 행은 불가능.
            - 오른쪽이 1 높은 경우: `왼쪽의 숫자 개수 >= L` 이면 가능 (아니면 불가능).
            - 오른쪽이 1 낮은 경우: `오른쪽의 숫자 개수 >= L` 이면 가능 (아니면 불가능).
        3. 끝까지 불가능 선언없이 도달했으면 가능한 경로 + 1
    - 각 열에 대해
        - 위쪽에서 시작해서 아래쪽으로 이동하면서 같은 로직.
"""
