# 포도주 시식
# 출처: https://hongcoding.tistory.com/48
n = int(input())
arr = [int(input()) for _ in range(n)]

# dp[i]: i번째 잔까지 마셨을때 가능한 최대 포도주
dp = [0] * n

# 초기화 및 예외처리
dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1]
if n > 2:
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])

# 핵심
for i in range(3, n):
    # 경우1: 현재와 1칸전을 마시고, 2칸전은 마시지 않는다. ('현재' + '1칸전' + '3칸전의 최대')
    # 경우2: 현재와 2칸전을 마시고, 1칸전은 마시지 않는다. ('현재' + '2칸전의 최대')
    # 경우3: 현재를 마시지 않는다. ('1칸전의 최대')
    dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2], dp[i - 1])

print(dp[n - 1])

"""
- 난이도: 실버1
- 분류: dp

- '2579번 - 계단 오르기'와 비슷한데, 경우의 수가 하나 더 추가된 문제 (현재 칸을 마시지 않는 경우)
"""
