# 목표: 서로 다른 무게의 공을 고르는 경우의 수
# 방법: 정렬해서 2중 for문으로 브루트포스. (시간초과일듯)

n, m = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if balls[i] != balls[j]:
            cnt += 1

print(cnt)
