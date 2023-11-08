# RGB거리 2
# 출처: https://velog.io/@yoopark/baekjoon-17404
INF = int(1e9)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = INF

for color in range(3):
    # 핵심: 시작지점을 고정하기 위해 나머지를 INF로 설정
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][color] = arr[0][color]

    # 1149번과 똑같이 돌리기
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    # 처음 집과 색이 다른 마지막 집만 확인
    for j in range(3):
        if j != color:
            answer = min(answer, dp[N - 1][j])

print(answer)

"""
- 난이도: 골드4
- 분류: dp

- 요약: 시작점을 고정하고 정답후보 찾기를 3번 반복
"""
