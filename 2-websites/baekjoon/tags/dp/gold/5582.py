# 공통 부분 문자열
A = " " + input()
B = " " + input()

# dp[i][j]: A의 i번째, B의 j번째 까지의 LCS substring
dp = [[0] * len(B) for _ in range(len(A))]
answer = 0

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])
        # 핵심: else 부분은 생략

print(answer)

"""
- 난이도: 골드5
- 분류: dp
- 소요 시간: 20분

- 요약: LCS인데 subsequence가 아니라 substring을 찾는 문제
- 핵심: 기존의 로직에서 else 부분을 생략
"""
