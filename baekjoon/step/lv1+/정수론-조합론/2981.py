# 검문
# 출처: https://tmdrl5779.tistory.com/94
import math

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
diffs = []
answer = []

# 모든 인접한 수끼리의 차이를 구함
for i in range(1, N):
    diffs.append(nums[i] - nums[i - 1])

# 차이의 gcd를 구함
gcd = diffs[0]
for i in range(1, N - 1):
    gcd = math.gcd(gcd, diffs[i])

# gcd의 약수를 구해서 정답에 추가
# 이때, 제곱근까지만 탐색하며 한번에 한쌍씩 구함
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        answer.append(i)
        answer.append(gcd // i)

answer.append(gcd)
answer = list(set(answer))  # 중복제거
answer.sort()
print(*answer)

"""
- 난이도: 골드4
- 분류: 정수론

요약
- 모든 '인접한 수끼리의 차이'의 최대공약수를 구하고, 해당 수의 1을 제외한 약수를 출력하면 된다.
- 약수를 구할때 최대공약수까지 구하면 시간초과이기 때문에, 제곱근까지만 탐색하면서 한쌍씩 구한다.

팁: "나눈 나머지가 모두 같다" -> GCD 떠올리기
"""
