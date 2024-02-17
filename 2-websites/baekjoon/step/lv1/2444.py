# 별 찍기 - 7
N = int(input())

for i in range(1, N):
    print(" " * (N - i) + "*" * (2 * i - 1))

for i in range(N, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))

"""
- 난이도: 브론즈3
- 분류: 심화 1 (구현)

- 주의: 별 뒤에 공백이 있으면 안 됨.
"""
