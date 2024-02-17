N = int(input())

# dp[i]: 자연수 i를 제곱수의 합으로 표현할때 항의 최소 개수
# 초기화: 자기자신 (모든 수를 1의 제곱의 합으로 표현한 것으로 생각)
dp = [i for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        square = j * j
        if square > i:
            break
        # 핵심: 모든 제곱수의 경우를 계산하고 최소값을 저장
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[N])

"""
- 난이도: 실버2
- 분류: dp

- 요약: 가능한 모든 경우들을 갱신하는 1차원 dp 유형
- 디버깅: 그리디하게 풀었더니 반례가 생김
- 참고: https://v3.leedo.me/devs/82
"""
