# 트리
N = int(input())
parent = list(map(int, input().split()))
target = int(input())

answer = 0


# 핵심1: 노드를 지우면 자손노드도 전부 제외
def dfs(idx, parent):
    parent[idx] = -2
    for i in range(len(parent)):
        if idx == parent[i]:
            dfs(i, parent)


dfs(target, parent)

# 핵심2: 리프노드 -> 부모로 한번도 등장하지 않은 것
for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        answer += 1
print(answer)

"""
- 난이도: 골드5
- 분류: 트리

- DFS 풀이 (BFS 보다 깔끔)
- 출처: https://wiselog.tistory.com/118
"""
