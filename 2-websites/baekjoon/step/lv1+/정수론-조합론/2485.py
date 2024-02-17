# 가로수
import math

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 정렬
arr.sort()

# 인접한 가로수끼리의 차를 구함
diffs = []
for i in range(1, N):
    diffs.append(arr[i] - arr[i - 1])

# 차의 gcd를 구함
gcd = diffs[0]
for d in diffs:
    gcd = math.gcd(gcd, d)

# 전체간격을 gcd로 나누어 필요한 총 가로수 구하기
# 더 심을 가로수 = 총 가로수 - 이미 심어진 가로수
print(((arr[-1] - arr[0]) // gcd) + 1 - N)

"""
- 난이도: 실버4
- 분류: 정수론
"""
