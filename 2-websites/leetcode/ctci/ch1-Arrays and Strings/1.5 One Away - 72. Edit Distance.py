class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        # 초기화
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i][0] = i
        for j in range(1, M + 1):
            dp[0][j] = j

        # 편집 거리 알고리즘
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                # 문자가 같으면 -> 왼쪽 위에 해당하는 수를 그대로 대입
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 문자가 다르면 -> 3가지 경우 중 최솟값 찾기
                # 1.삽입(왼쪽), 2.삭제(위쪽), 3.교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[N][M]


"""
- 난이도: Medium
- 분류: DP

- 백준 15483 '최소 편집' (골드3)
- 해설: https://joyjangs.tistory.com/38
"""
