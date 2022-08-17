N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

answer = min(data[0])
for d in data:
    row_min = min(d)
    answer = max(answer, row_min)

print(answer)
