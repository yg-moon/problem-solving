def solution(sizes):
    for size in sizes:
        size.sort()

    max_w = 0
    max_h = 0

    for w, h in sizes:
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h


"""
- 각 명함 정보 내부를 모두 정렬하고, 가로의 최대치와 세로의 최대치를 구해서 곱하기.
"""
