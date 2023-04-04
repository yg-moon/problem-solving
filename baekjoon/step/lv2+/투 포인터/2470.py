# 두 용액
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = N - 1

min_diff = int(2e9)  # 주의: 이번엔 최댓값이 1e9를 넘을수도 있다!
result = []

while l < r:
    cur_sum = arr[l] + arr[r]

    if abs(cur_sum) < min_diff:
        min_diff = abs(arr[l] + arr[r])
        result = [arr[l], arr[r]]

    # 용액의 합이 음수이면 l을 올림
    if cur_sum < 0:
        l += 1
    # 용액의 합이 양수이면 r을 내림
    else:
        r -= 1

print(*result)

"""
- 난이도: 골드5
- 분류: 투포인터
"""
