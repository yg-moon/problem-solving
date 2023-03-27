# 이항 계수 3
# 출처1: https://velog.io/@ledcost/백준-11401-파이썬-이항-계수-3-골드1-분할-정복
# 출처2: https://rhdtka21.tistory.com/123
N, K = map(int, input().split())
P = 1000000007


def fact(N):
    ret = 1
    for i in range(2, N + 1):
        ret = (ret * i) % P
    return ret


def power(n, k):
    if k == 0:
        return 1
    if k % 2 == 0:
        return (power(n, k // 2) ** 2) % P
    else:
        return (power(n, k // 2) ** 2 * n) % P


# nCk의 정의 + 나머지 연산 적용
top = fact(N)
bot = fact(N - K) * fact(K) % P

# 페르마의 소정리 활용
print(top * power(bot, P - 2) % P)

"""
- 난이도: 골드1
- 분류: 분할정복, 정수론

요약
1. 나머지 연산의 분배법칙
    - (A x B) % p = ((A % p) x (B % p)) % p
2. 페르마의 소정리
    - a^p ≡ a (mod p)
    -> a^p-2 ≡ a^-1 (mod p)
3. 따라서
    - nCk % p
    -> n!((n-k)!k!)^-1 % p 
    -> n!((n-k)!k!)^(p-2) % p 
"""
