# 사전 순 최대 공통 부분 수열
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

is_done = False
answer = []

while True:
    # Find the maximum common value in both sequences
    while True:
        if not A or not B:
            is_done = True
            break
        max_a = max(A)
        a_idx = A.index(max_a)
        max_b = max(B)
        b_idx = B.index(max_b)
        if max_a == max_b:
            break
        elif max_a > max_b:
            A.pop(a_idx)
        else:
            B.pop(b_idx)

    if is_done:
        break

    # Push the maximum value to ans
    answer.append(max_a)

    # Remove elements up to and including the maximum index
    A = A[a_idx + 1 :]
    B = B[b_idx + 1 :]

if answer:
    print(len(answer))
    print(*answer)
else:
    print(0)

"""
- 난이도: 골드4
- 분류: 그리디

요약
- LCS 응용처럼 보이지만 dp가 아닌 문제
"""
