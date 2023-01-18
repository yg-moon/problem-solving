# 테트로미노
N, M = map(int, (input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # 일자
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 네모
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # 총1
    [(0, 0), (1, 0), (2, 0), (2, -1)],  # 총2
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # 번개1
    [(0, 0), (1, 0), (1, -1), (2, -1)],  # 번개2
    [(0, 0), (1, 0), (1, -1), (1, 1)],  # 방향키
]
max_sum = 0


def rotate(mat):
    return list(map(list, zip(*mat[::-1])))


def fit(x, y, shape):
    global max_sum
    cur_sum = 0
    for dx, dy in shape:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            cur_sum += graph[nx][ny]
        else:
            break
    else:
        max_sum = max(max_sum, cur_sum)


for _ in range(4):
    graph = rotate(graph)
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            for shape in shapes:
                fit(i, j, shape)

print(max_sum)

"""
- 난이도: 골드4
- 분류: 브루트포스

요약
- 각 퍼즐조각을 상대좌표로 표현.
- 전체 그래프를 4번 회전해가며 모든 조각을 대입해보며 확인.
"""
