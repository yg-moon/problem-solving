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

# 예외처리
if N == 1:
    print(0)
    exit(0)

arr = prime_list(N)
l, r, answer = 0, 0, 0
cur_sum = arr[0]

while l <= r and r < len(arr):
    # 답을 찾았으면
    if cur_sum == N:
        answer += 1
    # 현재 합이 N 이하면
    if cur_sum <= N:
        r += 1
        if r < len(arr):
            cur_sum += arr[r]
    # 현재 합이 N 초과면
    else:
        cur_sum -= arr[l]
        l += 1

print(answer)

"""
- 난이도: 골드3
- 분류: 투포인터

- 누적합은 사용하지 않아도 됨
"""
