# BOJ 1929
from math import sqrt

M, N = map(int, input().split())
arr = [True for _ in range(N + 1)]
arr[0] = False
arr[1] = False

# 에라토스테네스의 체
for i in range(2, int(sqrt(N)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= N:
            arr[i * j] = False
            j += 1

for i in range(M, N + 1):
    if arr[i]:
        print(i)
