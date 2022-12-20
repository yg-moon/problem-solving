INF = int(1e9)


def solution(arr):
    N = len(arr) // 2 + 1  # 숫자의 개수
    max_dp = [[-INF] * N for _ in range(N)]
    min_dp = [[INF] * N for _ in range(N)]

    # 구간 (i,i)는 숫자 자기자신으로 초기화
    for i in range(N):
        max_dp[i][i] = int(arr[i * 2])
        min_dp[i][i] = int(arr[i * 2])

    # 매번 step의 크기만큼의 모든 구간들의 최댓값, 최솟값이 한번에 계산되는 방식
    for step in range(1, N):  # i와 j의 간격 step을 하나씩 늘리면서
        for i in range(N - step):
            j = i + step
            # i부터 j까지 돌면서, 괄호를 하나는 늘리고, 하나는 줄여서 각각의 범위 연산을 수행
            for k in range(i, j):
                if arr[k * 2 + 1] == "+":
                    # + 일 경우 최댓값은 최댓값 + 최댓값
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    # + 일 경우 최솟값은 최솟값 + 최솟값
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    # - 일 경우 최댓값은 최댓값 - 최솟값
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    # - 일 경우 최솟값은 최솟값 - 최댓값
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])

    return max_dp[0][N - 1]


"""
- 아이디어: 괄호 범위를 조절해나가면서 모든 경우의 최댓값을 계산.
    - ex. 10 - 5 + 7 + 9 - 20 - 30 + 10
        - case1 = 10 - (5 + 7 + 9 - 20 - 30 + 10)
        - case2 = (10 - 5) + (7 + 9 - 20 - 30 + 10)
        - case3 = (10 - 5 + 7) + (9 - 20 - 30 + 10)
        - case4 = (10 - 5 + 7 + 9) - (20 - 30 + 10)
        - case5 = (10 - 5 + 7 + 9 - 20) - (30 + 10)
        - case6 = (10 - 5 + 7 + 9 - 20 - 30) + 10
    - 설명
        - 주의: 괄호는 단순 계산이 아니라 ‘해당 수식을 계산한 최댓값’을 의미.
            - 따라서 괄호 내부는 차근차근 하나씩 계산해야 한다. (구현 참고)
        - 최종적으로 case1~6 중의 결과 중에서 최댓값이 정답.
- 핵심: 뺄셈 연산을 고려해서 찾아야 하므로, dp 배열 2개를 사용.
    - max_dp[i][j]: i번째 부터 j번째까지 구간의 연산의 최댓값
    - min_dp[i][j]: i번째 부터 j번째까지 구간의 연산의 최솟값
"""
