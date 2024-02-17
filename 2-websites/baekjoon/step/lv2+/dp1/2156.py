# 포도주 시식
N = int(input())
arr = [int(input()) for _ in range(N)]

# dp[i]: i번째 잔까지 마셨을때 가능한 최대 포도주
dp = [0] * 10001

# 초기화 및 예외처리
dp[0] = arr[0]
if N >= 2:
    dp[1] = arr[0] + arr[1]
if N >= 3:
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])

for i in range(3, N):
    # 핵심: 언제 arr 값을 쓰고, 언제 dp 값을 쓸 것인지
    # Case 1: 현재와 1칸전을 마시고, 2칸전은 마시지 않는 경우 ('현재' + '1칸전' + '3칸전의 최대')
    # Case 2: 현재와 2칸전을 마시고, 1칸전은 마시지 않는 경우 ('현재' + '2칸전의 최대')
    # Case 3: 현재를 마시지 않는 경우 ('1칸전의 최대')
    dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2], dp[i - 1])

print(dp[N - 1])

"""
- 난이도: 실버1
- 분류: dp

- 요약: 경우의 수를 나누어 생각하는 기본적인 유형
- 참고: https://hongcoding.tistory.com/48
"""
