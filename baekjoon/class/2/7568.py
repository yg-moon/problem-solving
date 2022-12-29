# 덩치
N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
result = []

for person1 in people:
    rank = 1
    for person2 in people:
        # 자신보다 몸무게와 키가 모두 큰 사람을 만날 때마다 등수가 하나씩 내려감
        if person1[0] < person2[0] and person1[1] < person2[1]:
            rank += 1
    result.append(rank)

print(*result)

"""
- 난이도: 실버5
- 분류: 브루트포스

디버깅
- 주의: 정렬로 풀려고 하면 안되고 완전탐색으로 풀어야한다. (몸무게와 키를 모두 비교해야하므로)
"""
