N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort(reverse=True)

for N in nums:
    print(N, end=" ")
