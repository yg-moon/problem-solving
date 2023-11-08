# 가장 긴 증가하는 부분 수열 4
# 출처: https://ji-gwang.tistory.com/278
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

# LIS 구하기
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# 역추적
answer = []
max_idx = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == max_idx:
        answer.append(arr[i])
        max_idx -= 1
answer.reverse()
print(*answer)

"""
- 난이도: 골드4
- 분류: dp

- LIS 최적해 출력
- (클래스5는 아니지만 14003번 역추적 로직 이해를 위해 추가)
"""
