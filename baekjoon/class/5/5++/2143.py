# 두 배열의 합
import bisect

T = int(input())
n = int(input())
A = [0] + list(map(int, input().split()))
m = int(input())
B = [0] + list(map(int, input().split()))

# 누적합 배열 만들기
psum_A = [0] * (n + 1)
psum_B = [0] * (m + 1)
for i in range(1, n + 1):
    psum_A[i] = psum_A[i - 1] + A[i]
for i in range(1, m + 1):
    psum_B[i] = psum_B[i - 1] + B[i]

# 모든 부배열의 합 구하기
lst_A = []
lst_B = []
for l in range(1, n + 1):
    for r in range(l, n + 1):
        lst_A.append(psum_A[r] - psum_A[l - 1])
for l in range(1, m + 1):
    for r in range(l, m + 1):
        lst_B.append(psum_B[r] - psum_B[l - 1])

# 이분탐색 활용 (count in range)
lst_A.sort()
lst_B.sort()
answer = 0
for i in range(len(lst_A)):
    l = bisect.bisect_left(lst_B, T - lst_A[i])
    r = bisect.bisect_right(lst_B, T - lst_A[i])
    answer += r - l

print(answer)

"""
- 난이도: 골드3
- 분류: 누적합, 이분탐색

- 핵심: T <= 10억이므로 이분탐색 필요
- 참고: https://imksh.com/78
"""
