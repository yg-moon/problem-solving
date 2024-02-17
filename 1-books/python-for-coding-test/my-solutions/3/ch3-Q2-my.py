# Naive approach
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
n1 = nums[0]
n2 = nums[1]
sum = 0

while M > 0:
    if M > K:
        sum += n1 * K
        sum += n2
        M -= K + 1
    else:
        sum += n1

print(sum)
