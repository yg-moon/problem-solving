# 가장 가까운 세 사람의 심리적 거리
from itertools import combinations


def dist(type1, type2):
    res = 0
    for i in range(4):
        if type1[i] != type2[i]:
            res += 1
    return res


T = int(input())

for _ in range(T):
    N = int(input())
    students = input().split()
    if N >= 33:
        print(0)
    else:
        min_dist = 12
        for idx1, idx2, idx3 in combinations(range(N), 3):
            stud1, stud2, stud3 = students[idx1], students[idx2], students[idx3]
            cur_dist = dist(stud1, stud2) + dist(stud2, stud3) + dist(stud1, stud3)
            min_dist = min(min_dist, cur_dist)
        print(min_dist)

"""
- 난이도: 실버1
- 분류: 브루트포스

핵심: 비둘기집 원리
- MBTI는 16개의 유형이 있으므로, n >= 33 부터는 항상 3명이 동일한 MBTI를 갖는 것이 보장된다.
"""
