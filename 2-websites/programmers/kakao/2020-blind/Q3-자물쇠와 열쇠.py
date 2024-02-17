def rotate(mat):
    return [list(row) for row in zip(*mat[::-1])]


def solution(key, lock):
    M = len(key)
    N = len(lock)
    P = (M - 1) + N + (M - 1)  # 패딩을 적용한 전체길이
    answer_slots = set()  # 자물쇠에서 채워야 하는 좌표

    # 패딩을 적용한 전체 그래프
    graph = [[-1] * P for _ in range(P)]
    for i in range(N):
        for j in range(N):
            graph[i + M - 1][j + M - 1] = lock[i][j]
            if lock[i][j] == 0:
                answer_slots.add((i + M - 1, j + M - 1))

    # 열쇠를 4번 돌리면서, 가능한 모든 칸에 꽂아보고 확인
    def check_all():
        nonlocal key
        for _ in range(4):
            key = rotate(key)
            for i in range(M + N - 1):
                for j in range(M + N - 1):
                    if did_match(i, j):
                        return True
        return False

    # 현재 위치에서 열쇠와 자물쇠의 모양을 확인
    def did_match(i, j):
        fit_slots = set()
        for x in range(M):
            for y in range(M):
                key_slot = key[x][y]
                lock_slot = graph[i + x][j + y]
                # 자물쇠의 돌기와 열쇠의 돌기가 만나면 안됨
                if lock_slot == 1 and key_slot == 1:
                    return False
                # 자물쇠의 홈과 열쇠의 돌기가 만나야 됨
                if lock_slot == 0 and key_slot == 1:
                    fit_slots.add((i + x, j + y))
        return fit_slots == answer_slots

    return check_all()


"""
- 분류: 완전탐색, 구현
- 시간: 3:50-5:20 (90분) (구현40분, 디버깅50분)
"""
