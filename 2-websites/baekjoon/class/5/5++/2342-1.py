# Dance Dance Revolution
arr = list(map(int, input().split()))

arr.pop()
N = len(arr)
INF = int(1e9)

# 핵심1: dp[지시사항 순서][왼발 위치][오른발 위치] = 최소 힘
dp = [[[INF] * 5 for _ in range(5)] for _ in range(N + 1)]
dp[0][0][0] = 0


# 핵심2: 어떤 발이 start -> end로 움직일때 드는 비용
def get_cost(start, end):
    if start == end:
        return 1
    elif start == 0:
        return 2
    elif abs(start - end) % 2 != 0:
        return 3
    else:
        return 4


# 핵심3: 점화식
for i in range(1, N + 1):
    nxt = arr[i - 1]  # 지시사항 (발의 다음위치)
    for l in range(5):
        for r in range(5):
            # 왼발을 움직이는 경우
            dp[i][nxt][r] = min(dp[i][nxt][r], dp[i - 1][l][r] + get_cost(l, nxt))
            # 오른발을 움직이는 경우
            dp[i][l][nxt] = min(dp[i][l][nxt], dp[i - 1][l][r] + get_cost(r, nxt))

answer = INF
for l in range(5):
    for r in range(5):
        answer = min(answer, dp[N][l][r])
print(answer)

"""
- 난이도: 골드3
- 분류: DP

- 핵심: 왼발, 오른발 경우를 나누어 점화식을 세우기
- 출처: https://dkrnfls.tistory.com/174
"""
