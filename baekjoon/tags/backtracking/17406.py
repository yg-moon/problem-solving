# 배열 돌리기 4
from copy import deepcopy

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ops = [list(map(int, input().split())) for _ in range(K)]
answer = int(1e9)


# '배열의 값' 구하기
def get_min_rowsum(arr):
    min_rowsum = int(1e9)
    for row in arr:
        min_rowsum = min(min_rowsum, sum(row))
    return min_rowsum


# 문제에서 원하는 회전 연산
def rotate(arr, r, c, s):
    x1, y1 = r - s - 1, c - s - 1
    x2, y2 = r + s - 1, c + s - 1

    # 가로와 세로의 길이중 짧은 것의 절반까지만
    for depth in range(min((x2 - x1), (y2 - y1)) // 2):
        # 매층마다 좌상단에서 시작해서, 한칸씩 이동하며 수정
        x = x1 + depth
        y = y1 + depth
        val = arr[x][y]

        for j in range(y1 + depth + 1, y2 - depth + 1):  # 상단
            y = j
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

        for j in range(x1 + depth + 1, x2 - depth + 1):  # 우변
            x = j
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

        for j in range(y2 - depth - 1, y1 + depth - 1, -1):  # 하단
            y = j
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

        for j in range(x2 - depth - 1, x1 + depth - 1, -1):  # 좌변
            x = j
            prev = arr[x][y]
            arr[x][y] = val
            val = prev

    return arr


# 회전 연산을 가능한 모든 순서로 해보기 (permutation)
def dfs(perm):
    global answer

    if len(perm) == len(ops):
        rotated_arr = deepcopy(arr)
        for i in perm:
            r, c, s = ops[i]
            rotated_arr = rotate(rotated_arr, r, c, s)
        answer = min(answer, get_min_rowsum(rotated_arr))
        return

    for i in range(len(ops)):
        if not visited[i]:  # 주의: 이거 빼먹지 말기
            visited[i] = True
            perm.append(i)
            dfs(perm)
            perm.pop()
            visited[i] = False


visited = [False] * len(ops)
dfs([])
print(answer)

"""
- 난이도: 골드4
- 분류: 백트래킹, 배열 회전

- 디버깅: 배열 회전이 제대로 안 됨
- 느낀점: 인덱스 처리는 off-by-1 오류에 주의해서 꼼꼼히 작성하기
"""
