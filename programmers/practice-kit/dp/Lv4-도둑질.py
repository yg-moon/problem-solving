def solution(money):
    N = len(money)

    # Case1: 첫 집을 털고, 마지막 집은 털지 않는 경우
    dp1 = [0] * N
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])
    dp1[N - 1] = dp1[N - 2]

    # Case2: 첫 집은 털지 않고, 그 뒤로는 원래대로 하는 경우
    dp2 = [0] * N
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])
    for i in range(2, N):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    # 두 경우를 통틀어서의 최댓값이 정답
    return max(max(dp1), max(dp2))


"""
- 원형구조: 시작점과 끝점이 안 만나게만 하면 된다.
"""
