import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, i, v, l=None, r=None):
        self.idx = i
        self.val = v
        self.left = l
        self.right = r


def solution(k, num, links):
    N = len(num)
    nodes = []
    new_links = []  # 백트래킹을 위해 링크 재정리
    answer = int(1e9)

    # 트리 만들기
    for i in range(N):
        nodes.append(Node(i, num[i]))
    for i, item in enumerate(links):
        l, r = item
        if l != -1:
            nodes[i].left = nodes[l]
            new_links.append((i, "L"))
        if r != -1:
            nodes[i].right = nodes[r]
            new_links.append((i, "R"))

    # k-1개 만큼 링크를 지우기
    def dfs(cnt, start):
        if cnt == k - 1:
            count()
            return

        for i in range(start, len(new_links)):
            idx, dir = new_links[i]
            # 링크 지우기
            if dir == "L":
                tmp = nodes[idx].left
                nodes[idx].left = None
            elif dir == "R":
                tmp = nodes[idx].right
                nodes[idx].right = None
            # 재귀
            dfs(cnt + 1, i + 1)
            # 링크 복구
            if dir == "L":
                nodes[idx].left = tmp
            elif dir == "R":
                nodes[idx].right = tmp

    # 모든 그룹의 인원수 파악하기
    def count():
        nonlocal answer
        visited = [False] * N
        max_sum = 0

        # 현재 노드를 기준으로 합 구하기
        def traverse(node):
            nonlocal cur_sum
            if node:
                visited[node.idx] = True
                cur_sum += node.val
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        # 모든 노드에 대해 최대 합 찾기
        for i in range(N):
            if not visited[i]:
                cur_sum = 0
                traverse(nodes[i])
                max_sum = max(max_sum, cur_sum)

        answer = min(answer, max_sum)

    dfs(0, 0)

    return answer


"""
- 분류: 트리
- 소요 시간: 10:10-11:40 (90분) (정확성 100점, 효율성 0점)

정확성
- 백트래킹: 모든 링크를 끊어보면서, 그룹의 개수가 k가 될때 최대그룹의 합의 최소치를 찾기 (k-1번만 끊으면 됨)
"""
