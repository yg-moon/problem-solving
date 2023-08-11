# 두 용액
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

l = 0
r = N - 1
min_diff = int(2e9)  # 주의: 이번엔 최댓값이 1e9를 넘을수도 있다!
result = []

while l < r:
    sum_val = arr[l] + arr[r]
    # 차이가 더 작다면 정답을 갱신
    if abs(sum_val) < min_diff:
        min_diff = abs(sum_val)
        result = [arr[l], arr[r]]
    # 합이 음수이면 l을 올림
    if sum_val < 0:
        l += 1
    # 합이 양수이면 r을 내림
    else:
        r -= 1

print(*result)

"""
- 난이도: 골드5
- 분류: 투포인터
"""
