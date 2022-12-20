INF = int(1e9)


def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]

    for j, i in puddles:  # 주의: 좌표가 반대로 되어있음
        dp[i - 1][j - 1] = INF

    for i in range(n):
        for j in range(m):
            # 웅덩이일 경우 패스
            if dp[i][j] == INF:
                continue
            left = dp[i][j - 1]  # 왼쪽 칸
            up = dp[i - 1][j]  # 위쪽 칸
            # 첫 행
            if i == 0:
                if j == 0:
                    continue
                elif j == 1:
                    dp[i][j] = 1
                elif left != INF:
                    dp[i][j] = left
            # 첫 열
            elif j == 0:
                if i == 1:
                    dp[i][j] = 1
                elif up != INF:
                    dp[i][j] = up
            # 나머지
            else:
                if left != INF:
                    dp[i][j] += left
                if up != INF:
                    dp[i][j] += up

    return dp[n - 1][m - 1] % 1000000007


"""
- 요약
    - dp[i][j]: 해당 위치까지 갈 수 있는 최단 경로의 개수
    - 첫 행과 첫 열을 잘 채우고, 나머지는 왼쪽 칸과 위쪽 칸의 값을 더해준다. (웅덩이 제외)
- 구현
    - dp 배열 채우기
        - 원칙: 현재 칸 / 왼쪽 칸 / 위쪽 칸이 웅덩이일 경우 무시.
        - 첫 행: (0,1)은 1로 설정하고, 나머지는 왼쪽 칸의 값을 그대로 사용.
        - 첫 열: (1,0)은 1로 설정하고, 나머지는 위쪽 칸의 값을 그대로 사용.
        - 나머지: 왼쪽 칸과 위쪽 칸의 값을 더해줌.
    - 주의: 웅덩이의 좌표가 반대로 되어있으므로 처음에 잘 입력하기.
"""
