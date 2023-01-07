# 2xn 타일링
n = int(input())

# dp[i]: 2*i 크기의 직사각형을 주어진 타일로 채우는 방법의 수
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)

"""
- 난이도: 실버3
- 분류: dp

- 해설: https://duckracoon.tistory.com/entry/백준-11726-2xn-타일링-해설-python
"""
