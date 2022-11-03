def solution(sizes):
    for size in sizes:
        size.sort()

    wallet_w = 0
    wallet_h = 0

    for w, h in sizes:
        wallet_w = max(wallet_w, w)
        wallet_h = max(wallet_h, h)

    return wallet_w * wallet_h


"""
- 각 명함 정보 내부를 모두 정렬하고, 가로의 최대치와 세로의 최대치를 구해서 곱하기.
"""
