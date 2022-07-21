# BOJ 14888
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

INF = 1e9
max_res = -INF
min_res = INF


def dfs(res, nums):
    global add, sub, mul, div, max_res, min_res
    if not nums:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
    else:
        if add > 0:
            add -= 1
            dfs(res + nums[0], nums[1:])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(res - nums[0], nums[1:])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(res * nums[0], nums[1:])
            mul += 1
        if div > 0:
            next_res = 0
            if res < 0:
                next_res = -(-res // nums[0])
            else:
                next_res = res // nums[0]
            div -= 1
            dfs(next_res, nums[1:])
            div += 1


dfs(nums[0], nums[1:])

print(max_res)
print(min_res)
