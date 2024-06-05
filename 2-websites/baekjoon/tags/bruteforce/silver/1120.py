# 문자열
A, B = input().split()
min_diff = int(1e9)

# i: 시작점, j: 상대적 위치
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    min_diff = min(min_diff, cnt)

print(min_diff)

"""
- 난이도: 실버4
- 분류: 문자열, 브루트포스

- 풀이:
a = abcd
b = abcdef 이면
(abcd)ef -> cnt = 0
a(bcde)f -> cnt = 4
ab(cdef) -> cnt = 4

- 참고: https://yoonsang-it.tistory.com/55
"""
