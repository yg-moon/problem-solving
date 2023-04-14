# 팰린드롬?
# 출처: https://cocoon1787.tistory.com/326
import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))  # 문제가 1-idx 이므로 맞춰주기
M = int(input())

# dp[i][j]: 구간 (i,j)가 팰린드롬인지 여부 (0 or 1)
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 초기화
for i in range(1, N + 1):
    # 한자리 수는 자체로 팰린드롬
    dp[i][i] = 1
    # 연속된 두자리 수는 팰린드롬
    if i != 1 and arr[i - 1] == arr[i]:
        dp[i - 1][i] = 1

# 핵심: 구간 (X, Y)가 팰린드롬 <=> 구간 (X+1, Y-1)가 팰린드롬이고, arr[X] = arr[Y]
# gap: 구간의 길이, start: 구간의 시작점
for gap in range(2, N):
    for start in range(1, N - gap + 1):
        if dp[start + 1][start + gap - 1] == 1 and arr[start] == arr[start + gap]:
            dp[start][start + gap] = 1

# 출력
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])

"""
- 난이도: 골드4
- 분류: dp

팁
- 2차원 dp임을 눈치채기
- 구간의 크기와 시작점을 기준으로 순회하기 (구간 쪼개기 유형처럼)
"""
