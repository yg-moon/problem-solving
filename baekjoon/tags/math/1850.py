# 최대공약수


# 유클리드 호제법
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


A, B = map(int, input().split())
res = gcd(A, B)
print("1" * res)  # 주의: int로 변환하면 시간초과

"""
- 난이도: 실버1
- 분류: 수학, 정수론

- 핵심: 두 수의 gcd가 아니라, 두 수의 1의 개수의 gcd만 구하면 됨
- 참고: https://claude-u.tistory.com/404
"""
