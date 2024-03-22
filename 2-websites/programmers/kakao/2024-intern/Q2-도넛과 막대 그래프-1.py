from collections import defaultdict


def solution(edges):
    # 진입간선, 진출간선
    idg = defaultdict(int)
    odg = defaultdict(int)
    for a, b in edges:
        odg[a] += 1
        idg[b] += 1

    created = 0
    g1 = 0
    g2 = 0
    g3 = 0
    total = 0

    # 생성된 정점
    for node in odg:
        if idg[node] == 0 and odg[node] >= 2:
            created = node
            total = odg[node]
            break

    # 생성된 정점과 연결된 간선을 삭제
    for a, b in edges:
        if a == created:
            odg[a] -= 1
            idg[b] -= 1

    # 각 그래프 개수 찾기
    for node in idg:
        if node != created:
            if odg[node] == 0:
                g2 += 1
            elif idg[node] == 2 and odg[node] == 2:
                g3 += 1

    # 팁: 간접적으로 구하기
    g1 = total - g2 - g3

    return [created, g1, g2, g3]


"""
- 분류: 그래프

해설
- 그래프를 순회할 필요없이, 진입간선과 진출간선을 통해 특징을 파악
"""
