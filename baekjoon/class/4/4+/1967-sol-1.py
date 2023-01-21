# 트리의 지름
# 출처: https://my-coding-notes.tistory.com/285
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
diameter = 0

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))

# DFS로 리프노드까지 내려가서 해당 노드의 가중치를 리턴
def dfs(node, weight):
    global diameter
    left, right = 0, 0

    # 자식이 있는 노드는 왼쪽과 오른쪽 최장경로를 계산
    for child, wei in tree[node]:
        res = dfs(child, wei)
        if left <= right:
            left = max(left, res)
        else:
            right = max(right, res)

    # 현재노드 기준으로 트리의 지름: left + right
    # 최종 정답: 전체 트리에서의 최대치
    diameter = max(diameter, left + right)

    # 상태값: 리프노드부터 현재노드까지의 최장경로
    # 왼쪽과 오른쪽 경로 중 더 큰 것을 리턴
    return max(left + weight, right + weight)


dfs(1, 0)

print(diameter)


"""
- 난이도: 골드4
- 분류: 트리

- 아이디어: 트리의 지름 = 왼쪽 최장경로 + 오른쪽 최장경로
"""
