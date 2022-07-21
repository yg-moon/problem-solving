# Kakao 2020
# 시계방향 90도 회전
def rotate(key):
    size = len(key)
    rotated = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated[j][size - 1 - i] = key[i][j]
    return rotated


def solution(key, lock):
    N = len(lock)
    M = len(key)
    P = N + 2 * (M - 1)
    graph = [[0] * P for _ in range(P)]
    lock_zero_pos = []  # 자물쇠에서 0인 좌표 목록

    # 자물쇠를 padding: 범위 밖은 2로 처리
    for x in range(P):
        for y in range(P):
            if x < M - 1 or x > P - M or y < M - 1 or y > P - M:
                graph[x][y] = 2
            else:
                graph[x][y] = lock[x - (M - 1)][y - (M - 1)]
                if graph[x][y] == 0:
                    lock_zero_pos.append((x, y))
    lock_zero_pos.sort()

    # 돌려가면서 열쇠 꽂기
    answer = False
    for _ in range(4):
        key = rotate(key)
        for x in range(P - (M - 1)):  # 주의: range(P)로 하면 범위를 벗어남
            for y in range(P - (M - 1)):
                key_match_pos = []  # 짝이 맞는 좌표 목록
                overlap = False  # 돌기가 겹치는지 확인
                for a in range(M):
                    for b in range(M):
                        # 주의: mat[x][y]가 아님!
                        if graph[x + a][y + b] == 0 and key[a][b] == 1:
                            key_match_pos.append((x + a, y + b))
                        elif graph[x + a][y + b] == 1 and key[a][b] == 1:
                            overlap = True
                key_match_pos.sort()
                if not overlap and lock_zero_pos == key_match_pos:
                    answer = True

    return answer
