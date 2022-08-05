# 출처: 이코테
N = int(input())

dp = [0] * N
dp[0] = 1

# 2배, 3배, 5배 관리를 위한 인덱스
i2 = i3 = i5 = 0
# 2배, 3배, 5배 각각 다음 못생긴 수 후보
next2, next3, next5 = 2, 3, 5

for i in range(1, N):
    # 후보 중 가장 작은 것을 선택
    dp[i] = min(next2, next3, next5)
    # 해당 배수의 인덱스 및 후보 업데이트
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

# n번째 못생긴 수를 출력
print(dp[N - 1])
