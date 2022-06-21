import bisect

n = int(input())
shop_list = list(map(int, input().split()))
m = int(input())
user_list = list(map(int, input().split()))

shop_list.sort()

for e in user_list:
    idx = bisect.bisect_right(shop_list, e) - 1
    if 0 <= idx < n and shop_list[idx] == e:
        print("yes", end=" ")
    else:
        print("no", end=" ")
