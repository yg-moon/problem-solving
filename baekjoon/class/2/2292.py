# 벌집
N = int(input())

if N == 1:
    print(1)
else:
    cur = 2
    offset = 6
    steps = 1
    while cur <= N:
        cur += offset
        offset += 6
        steps += 1
    print(steps)

"""
- 난이도: 브론즈2
- 분류: 수학

패턴
- N = 1 일때, 답: 1
- N = 2~7 일때, 답: 2
- N = 8~19 일때, 답: 3
- N = 20~37 일때, 답: 4
- N = 38~61 일때, 답: 5

- N의 시작점을 보면 1, 2, 8, 20, 38, ...
- 즉, 6, 12, 18, ... 씩 늘어나는 계차수열.
"""
