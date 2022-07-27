# from 이코테
for T in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 2차원 배열 dp: arr 내용으로 초기화
    dp = []
    idx = 0
    for i in range(N):
        dp.append(arr[idx : idx + M])
        idx += M

    # DP
    for j in range(1, M):
        for i in range(N):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == N - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            # 계산
            dp[i][j] += max(left_up, left_down, left)

    # 마지막 열의 최댓값
    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][M - 1])
    print(answer)
