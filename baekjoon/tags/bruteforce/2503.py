# 숫자 야구
from itertools import permutations

N = int(input())
queries = [list(map(int, input().split())) for _ in range(N)]

perms = list(permutations(list("123456789"), 3))
impossible = set()

# 모든 질문에 대해
for num, strike, ball in queries:
    num = str(num)
    # 모든 세자리 숫자에 대해
    for perm in perms:
        cur_strike = 0
        cur_ball = 0
        # 스트라이크와 볼의 개수를 세고
        for i in range(3):
            if perm[i] == num[i]:
                cur_strike += 1
            elif num[i] in perm:
                cur_ball += 1
        # 맞지 않는 경우는 제외
        if cur_strike != strike or cur_ball != ball:
            impossible.add((perm))

print(len(perms) - len(impossible))

"""
- 난이도: 실버3
- 분류: 브루트포스

요약
- 가능한 모든 경우를 생성하고, 전체에서 틀린 답의 개수를 뺀다.
- 참고: https://yuna0125.tistory.com/115

디버깅
- 너무 어렵게 생각했다... 사람이 푸는 것처럼 해결하려고 했다.
- n이 작다면 항상 완전탐색을 고려해보자. (9P3 = 504)
"""
