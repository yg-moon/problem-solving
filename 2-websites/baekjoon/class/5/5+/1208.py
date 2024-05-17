# 부분수열의 합2
from bisect import bisect_left, bisect_right
from itertools import combinations


# arr에서 x의 개수를 계산 (이분탐색)
def count(arr, x):
    return bisect_right(arr, x) - bisect_left(arr, x)


# arr의 가능한 모든 부분집합을 계산
def calc_subset(arr):
    subset = []
    for i in range(1, len(arr) + 1):
        for comb in combinations(arr, i):
            subset.append(sum(comb))
    subset.sort()
    return subset


N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 수열을 절반으로 나누기
left = arr[: N // 2]
right = arr[N // 2 :]

# 각 절반에 대해 가능한 모든 부분집합을 계산
A = calc_subset(left)
B = calc_subset(right)
answer = 0

# a+b=S가 되는 개수를 계산 (MITM)
for a in A:
    target = S - a
    answer += count(B, target)

# A, B 자체적으로 S를 갖는 경우를 계산
answer += count(A, S)
answer += count(B, S)

print(answer)

"""
- 난이도: 골드1
- 분류: 이분탐색, Meet in the Middle

- 참고: https://velog.io/@yiseull/백준-1208번-부분수열의-합-2-Python
"""
