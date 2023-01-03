# 1, 2, 3 더하기
from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())

    # dp[i]: 정수 i를 1,2,3의 합으로 표현하는 모든 tuple의 set.
    dp = defaultdict(set)
    dp[1] = {(1,)}  # 주의: 원소가 1개인 튜플을 만들고 싶다면 끝에 , 를 붙일 것
    dp[2] = {(1, 1), (2,)}
    dp[3] = {(1, 1, 1), (1, 2), (2, 1), (3,)}

    for i in range(4, n + 1):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    new_pair = list(x)
                    new_pair.extend(list(y))
                    new_pair = tuple(new_pair)
                    if new_pair not in dp[i]:
                        dp[i].add(new_pair)

    print(len(dp[n]))

"""
- 난이도: 실버3
- 분류: dp

- (정답을 확인하니 쓸데없이 복잡하게 풀었다...)
"""
