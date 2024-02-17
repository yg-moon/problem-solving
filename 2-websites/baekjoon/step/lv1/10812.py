# 바구니 순서 바꾸기
N, M = map(int, input().split())
arr = [0] * N

for i in range(N):
    arr[i] = i + 1

for _ in range(M):
    i, j, k = map(int, input().split())
    arr[i - 1 : j] = arr[k - 1 : j] + arr[i - 1 : k - 1]

print(*arr)

"""
- 난이도: 브론즈2
- 분류: 심화 1 (구현)

- 주의: 파이썬 슬라이싱 범위 생각하기. (끝범위 미포함)
"""
