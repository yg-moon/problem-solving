import bisect

N = int(input())
shop_list = list(map(int, input().split()))
M = int(input())
user_list = list(map(int, input().split()))

shop_list.sort()

for item in user_list:
    idx = bisect.bisect_right(shop_list, item) - 1
    if 0 <= idx < N and shop_list[idx] == item:
        print("yes", end=" ")
    else:
        print("no", end=" ")
