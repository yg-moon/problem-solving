# 부분합
N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 누적합을 위해 1-idx 맞춰주기

psum = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i]

l = 1
r = 1  # 주의1: 처음에 정답이 존재할 수 있으므로 r = 2 가 아님
INF = int(1e9)
min_len = INF

while l <= r and r <= N:  # 주의2: 길이가 1인것도 세야 하므로 l < r 이 아님
    cur_sum = psum[r] - psum[l - 1]
    # 구간합이 S이상이면, 정답을 갱신하고 l을 올림
    if cur_sum >= S:
        min_len = min(min_len, r - l + 1)
        l += 1
    # 구간합이 S미만이면, r을 올림
    else:
        r += 1

print(min_len if min_len != INF else 0)

"""
- 난이도: 골드4
- 분류: 누적합, 투포인터

- 예외 케이스 처리가 중요했던 문제
"""
