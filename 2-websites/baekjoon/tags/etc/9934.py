# 완전 이진 트리
from collections import deque

K = int(input())
path = list(map(int, input().split()))

# tree[node][0]: left child
# tree[node][1]: right child
tree = [[0] * 2 for _ in range(2**K)]
root = path[len(path) // 2]


# traversal 결과가 주어졌을 때 원본 트리를 만들기
def dfs(arr):
    if not arr:
        return 0
    mid_idx = len(arr) // 2  # 주의: 인덱스랑 값이랑 헷갈리지 말기
    mid = arr[mid_idx]
    tree[mid][0] = dfs(arr[:mid_idx])
    tree[mid][1] = dfs(arr[mid_idx + 1 :])
    return mid


dfs(path)


# 트리를 층별로 출력하기
def print_tree():
    cur_q = deque([root])
    while cur_q:
        print(*cur_q)
        nxt_q = deque()  # 주의: 매번 새로 생성하기
        while cur_q:
            node = cur_q.popleft()
            for i in range(2):
                if tree[node][i] != 0:
                    nxt_q.append(tree[node][i])
        cur_q = nxt_q


print_tree()

"""
- 난이도: 실버1
- 분류: 트리, 재귀
"""
