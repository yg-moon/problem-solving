# 실패. (논리가 잘못됨)
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()

if N == 1:
    print(0)
elif N == 2:
    print(nums[0] + nums[1])
else:
    curr_sum = nums[0] + nums[1]
    total = curr_sum
    for i in range(2, N):
        curr_sum += nums[i]
        total += curr_sum
    print(total)
