# 실패. (논리가 잘못됨)
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    arr = []
    # 입력값을 2차원 배열 형태로 저장
    idx = 0
    for _ in range(N):
        temp = []
        for _ in range(M):
            temp.append(data[idx])
            idx += 1
        arr.append(temp)

    # DP
    dp = [[0] * M for _ in range(N)]
    di = [-1, 0, 1]
    dj = [1, 1, 1]

    for i in range(N):
        dp[i][0] = arr[i][0]
        for j in range(M - 1):
            for k in range(3):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + arr[ni][nj])

    # 마지막 열의 최댓값
    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][M - 1])
    print(answer)
