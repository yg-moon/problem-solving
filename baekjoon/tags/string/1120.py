# 문자열
# 출처: https://yoonsang-it.tistory.com/55
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

- 예시:
a = abcd
b = abcdef 이면

(abcd)ef -> cnt = 0
a(bcde)f -> cnt = 4
ab(cdef) -> cnt = 4

- 주의: 브루트포스라고 해서 진짜 너무 무식하게 풀면 안 된다.
- 팁: 이렇게 슬라이딩 윈도우처럼 푸는 방식 기억하기.
"""
