# 주식
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = arr[-1]
    answer = 0

    # 역방향 탐색
    for i in range(N - 2, -1, -1):
        # 최대 가격보다 낮으면 판매
        if arr[i] <= max_val:
            answer += max_val - arr[i]
        # 최대 가격보다 높으면 최대 가격을 갱신
        else:
            max_val = arr[i]

    print(answer)

"""
- 난이도: 실버2
- 분류: 그리디

- 핵심: 역방향으로 탐색하면서 바로 판매
- 참고: https://tussle.tistory.com/936
"""
