# Σ
# 출처1: https://rccode.tistory.com/entry/Python-백준-13172번-∑
# 출처2: https://0422.tistory.com/99
M = int(input())
X = 1000000007
answer = 0


def solve(n, s):
    return s * pow(n, X - 2) % X


def pow(num, exp):
    if exp == 1:
        return num
    if exp % 2 == 0:
        root = pow(num, exp // 2)
        return root * root % X
    else:
        return num * pow(num, exp - 1) % X


for _ in range(M):
    N, S = map(int, input().split())
    answer += solve(N, S)
    answer %= X

print(answer)

"""
- 난이도: 골드4
- 분류: 수학 (분할정복을 이용한 거듭제곱)

요약
- 1. b^(X - 2) ≡ b^(-1) (mod X)
- 2. (기댓값) = (a x b^(-1)) mod 1,000,000,007
- 즉, a*b^(X-2) % X (이때, X = 1,000,000,007)를 시간안에 해결하는 문제.

- 'BOJ #1629 - 곱셈'처럼 풀어도 되고, 이번 문제처럼 풀어도 된다.
"""
