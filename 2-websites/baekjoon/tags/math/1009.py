# 분산처리
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    result = a
    # 핵심: 반복문을 통해 거듭제곱 계산
    for _ in range(b - 1):
        result = (result * a) % 10
    # 주의: b가 1일수도 있으므로 한번 더 나눠주기
    result %= 10

    if result == 0:
        print(10)
    else:
        print(result)

"""
- 난이도: 브론즈2
- 분류: 수학

- 아주 큰 거듭제곱을 처리하는 방법: 반복문
"""
