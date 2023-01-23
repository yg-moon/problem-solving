# 소수 구하기
M, N = map(int, input().split())
arr = [True for _ in range(N + 1)]
arr[0] = False
arr[1] = False

# 에라토스테네스의 체
for i in range(2, int(N**0.5) + 1):
    if arr[i]:
        # 핵심: i*2부터 N까지, i씩 증가하며 검사
        for j in range(i * 2, N + 1, i):
            arr[j] = False

for i in range(M, N + 1):
    if arr[i]:
        print(i)

"""
- 난이도: 실버3
- 분류: 수학
"""
