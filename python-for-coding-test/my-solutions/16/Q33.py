# BOJ 14501
# from 이코테
N = int(input())
t = [0]
p = [0]
dp = [0] * (N + 2)  # 1-index 사용
max_val = 0

for _ in range(N):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 뒤쪽부터 거꾸로 확인
for i in range(N, 0, -1):
    time = t[i] + i  # 상담을 마친 날
    # 상담이 기간 안에 끝나는 경우
    if time <= N + 1:
        # dp[i]: i번째 날부터 시작했을 때, 마지막 날까지 낼 수 있는 최대 수익.
        dp[i] = max(max_val, p[i] + dp[time])
        # 현재까지의 최댓값 업데이트
        max_val = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_val

print(max_val)
