from collections import defaultdict


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def solution(n, wires):
    min_diff = int(1e9)

    # 매번 전선을 하나씩 제외하며 전력망 구축
    for skip in range(n - 1):
        parent = defaultdict(int)
        cnt_dic = defaultdict(int)  # 각 전력망의 송전탑 개수

        # 부모는 자기 자신으로 초기화
        for i in range(n):
            parent[i] = i

        # 모든 노드를 union
        for i in range(n - 1):
            if i == skip:
                continue
            union(wires[i][0], wires[i][1], parent)

        # 모든 노드에 find
        for i in range(n):
            cnt_dic[find(i, parent)] += 1

        # 차이의 최솟값을 갱신
        cnt_list = list(cnt_dic.values())
        min_diff = min(min_diff, abs(cnt_list[0] - cnt_list[1]))

    return min_diff


"""
- 각 전선을 한번씩 제외하면서, union-find로 전력망을 구축하고 개수 파악.
"""
