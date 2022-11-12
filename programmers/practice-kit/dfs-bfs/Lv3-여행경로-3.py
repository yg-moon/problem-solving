from collections import defaultdict


def solution(tickets):
    # {출발점: [도착점 목록]}
    graph = defaultdict(list)
    for src, dst in sorted(tickets):
        graph[src].append(dst)

    route, stack = [], ["ICN"]
    while stack:
        # 현재 스택의 끝 공항에서 갈 수 있는 도착점을 하나 뽑아서 또 스택에 추가.
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        # 더 이상 도착점이 없다면, 스택에서 하나를 뽑아서 정답 경로에 추가.
        route.append(stack.pop())

    # 결과가 거꾸로 된 상태이므로 뒤집기
    return route[::-1]


"""
- LeetCode #332
- 스택 (반복 풀이)
"""
