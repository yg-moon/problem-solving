# 소수의 연속합
def prime_list(n):
    # 에라토스테네스의 체
    a = [True] * (n + 1)
    a[0] = False
    a[1] = False
    for i in range(2, int(n**0.5) + 1):
        if a[i] == True:
            for j in range(i * 2, n + 1, i):
                a[j] = False
    return [i for i in range(n + 1) if a[i]]


N = int(input())
arr = [0] + prime_list(N)
psum = [0] * len(arr)

for i in range(1, len(psum)):
    psum[i] = psum[i - 1] + arr[i]

l, r = 1, 1
answer = 0

while l <= r and r < len(psum):
    cur_sum = psum[r] - psum[l - 1]
    if cur_sum == N:
        answer += 1
    # 구간합이 N 미만이면 r을 올림
    if cur_sum < N:
        r += 1
    # 구간합이 N 이상이면 l을 올림
    else:
        l += 1

print(answer)

"""
- 난이도: 골드3
- 분류: 투포인터
"""
