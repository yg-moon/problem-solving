# 숫자 야구
from itertools import permutations

N = int(input())
queries = [list(map(int, input().split())) for _ in range(N)]
perms = list(permutations(list("123456789"), 3))
impossible = set()

for num, strike, ball in queries:
    num = str(num)
    for perm in perms:
        cur_strike = 0
        cur_ball = 0
        for i in range(3):
            if perm[i] == num[i]:
                cur_strike += 1
            elif num[i] in perm:
                cur_ball += 1
        if cur_strike != strike or cur_ball != ball:
            impossible.add((perm))

print(len(perms) - len(impossible))

"""
- 난이도: 실버3
- 분류: 완전탐색

핵심
- 너무 어렵게 생각했다... 사람이 푸는 것처럼 해결하려고 했다.
- n이 작다면 항상 완전탐색을 고려해보자. (9P3 = 504)

요약
- 가능한 모든 경우(서로 다른 숫자로 구성된 세자리 수)를 생성한다.
- 매 질문에 대해 틀린 답이 나오는 경우를 전체에서 제외한다.
- 참고: https://yuna0125.tistory.com/115
"""
