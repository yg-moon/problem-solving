# 수열 정렬
N = int(input())
A = list(map(int, input().split()))

info = []
P = [0] * N

# A를 (val, idx)로 묶은 이후 val 기준으로 오름차순 정렬
for i in range(N):
    info.append((A[i], i))

info.sort()

# P[A에서 현재순서 숫자의 인덱스값] = 현재순서
for i in range(N):
    P[info[i][1]] = i

print(*P)

"""
- 난이도: 실버4
- 분류: 정렬

- 설명: B[P[i]] = A[i]에서 B가 오름차순이어야 하므로,
    A를 (val, idx)로 묶어서 val 기준으로 오름차순 정렬 이후,
    A의 해당 idx들이 어떤 순서로 등장해야 하는지 P에 기록하는 것.
- 디버깅: 순열을 이용한 완전탐색은 N <= 50 이기 때문에 시간초과
"""
