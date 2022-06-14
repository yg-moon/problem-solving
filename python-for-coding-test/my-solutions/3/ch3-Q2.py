# Naive approach
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
n1 = nums[0]
n2 = nums[1]
sum = 0

while m > 0:
    if m > k:
        sum += n1 * k
        sum += n2
        m -= k + 1
    else:
        sum += n1

print(sum)
