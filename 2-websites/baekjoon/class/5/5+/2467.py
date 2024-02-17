# 용액
N = int(input())
arr = list(map(int, input().split()))

l = 0
r = N - 1
min_diff = int(2e9)
answer = []

while l < r:
    val = arr[l] + arr[r]
    if abs(val) < min_diff:
        min_diff = abs(val)
        answer = [arr[l], arr[r]]
    if val <= 0:
        l += 1
    else:
        r -= 1

print(*answer)

"""
- 난이도: 골드5
- 분류: 투포인터

- '2470번: 두 용액'과 거의 동일한 문제, 입력값이 정렬되어 주어진다는 차이점만 있음.
"""
