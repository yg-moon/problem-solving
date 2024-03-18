# 양팔저울
N = int(input())
weights = list(map(int, input().split()))
K = int(input())
marbles = list(map(int, input().split()))

# dp[i][j]: i번째 추까지 사용했을때, j의 무게를 만들 수 있는지 여부
dp = [[-1] * 15001 for _ in range(31)]


def dfs(i, w):
    # 주어진 추의 개수를 초과했거나, 이미 계산한 경우라면 리턴 (Top-down)
    if i > N or dp[i][w] != -1:
        return

    # i번째 추까지 사용하여 무게 w를 만들 수 있다는 것을 표시
    dp[i][w] = 1

    # 핵심: 경우의 수
    # 1. 추의 무게를 더하기
    # 2. 추의 무게를 빼기
    # 3. 추를 사용하지 않기(!)
    dfs(i + 1, w + weights[i - 1])
    dfs(i + 1, abs(w - weights[i - 1]))
    dfs(i + 1, w)


dfs(0, 0)

res = []
for m in marbles:
    if m > 30 * 500:
        res.append("N")
    elif dp[N][m] == 1:
        res.append("Y")
    else:
        res.append("N")
print(*res)

"""
- 난이도: 골드3
- 분류: dp
- 유형: Top-down 냅색 + dp배열 의미설정

참고
- 출처: https://my-coding-notes.tistory.com/157
- 설명: https://nbalance97.tistory.com/110
"""
