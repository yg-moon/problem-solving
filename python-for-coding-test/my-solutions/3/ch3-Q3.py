# 책 풀이와 동일
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

answer = min(data[0])
for d in data:
    row_min = min(d)
    answer = max(answer, row_min)

print(answer)
