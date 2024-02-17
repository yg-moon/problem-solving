# 가장 긴 증가하는 부분 수열
N = int(input())
A = list(map(int, input().split()))

# LIS
dp = [1] * N  # dp[i]: arr[i]를 마지막 원소로 갖는 부분 수열의 최대 길이
for i in range(N):  # i는 N까지, j는 i까지 올라가면서 확인
    for j in range(i):
        if A[j] < A[i]:  # 자신(i)보다 왼쪽(j)에 작은게 있으면 dp 값을 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

"""
- 난이도: 실버2
- 분류: dp
"""
