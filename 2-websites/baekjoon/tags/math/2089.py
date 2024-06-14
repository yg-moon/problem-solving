# -2진수
N = int(input())

if N == 0:
    print(0)
    exit()

result = []

while N:  # 핵심1
    if N % (-2) == 0:
        result.append("0")
        N //= -2
    else:
        result.append("1")
        N = N // -2 + 1  # 핵심2

print("".join(result[::-1]))

"""
- 난이도: 실버2
- 분류: 수학, 정수론

진수 계산법 규칙
- 항상 뺄셈으로 처리
- 항상 나머지는 양수

참고
- https://suri78.tistory.com/119
"""
