N = int(input())
data = [list(input().split()) for _ in range(N)]

data.sort(key=lambda x: x[1])

for d in data:
    print(d[0], end=" ")
