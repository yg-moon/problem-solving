def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 첫 행
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            # 마지막 행
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            # 나머지
            else:
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    return max(triangle[len(triangle) - 1])


"""
- dp[i][j]: 해당 위치까지 진행했을 때 경로의 최댓값
- 핵심: 모든 값은 위쪽 or 왼쪽 위에서만 들어올 수 있음. (단, 각 행의 끝값들은 예외처리 필요)
    - 이전에서 올 수 있는 가능성 중 최대치를 선택하여 자신과 합을 기록하는 방식.
"""
