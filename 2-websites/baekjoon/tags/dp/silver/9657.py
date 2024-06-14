# 돌 게임 3
N = int(input())

# dp[i]: 돌 i개로 게임할 때 SK가 이기는지
dp = [False] * 1001

# 초기화
dp[1] = True
dp[3] = True
dp[4] = True

for i in range(5, N + 1):
    # 핵심: 첫 턴에 어떻게 돌을 가져가든 다음 차례에서 이기는 경우, CY의 승리
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = False
    else:
        dp[i] = True

if dp[N]:
    print("SK")
else:
    print("CY")

"""
- 난이도: 실버3
- 분류: dp, 게임이론

참고
- https://jewoo-dev.tistory.com/31
"""
