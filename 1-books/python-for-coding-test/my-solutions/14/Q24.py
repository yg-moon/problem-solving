# BOJ 18310
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 중간값(median)
print(arr[(N - 1) // 2])
