# 통나무 건너뛰기
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    front = []
    back = []
    mid = arr[0]

    for i in range(1, N):
        if i % 2 == 0:
            back.append(arr[i])
        else:
            front.append(arr[i])

    front.reverse()

    result = front
    result.append(mid)
    result.extend(back)

    max_diff = abs(result[0] - result[-1])
    for i in range(N - 1):
        max_diff = max(max_diff, abs(result[i] - result[i + 1]))

    print(max_diff)

"""
- 난이도: 실버1
- 분류: 그리디, 정렬

풀이
- 가운데 가장 큰 수를 넣고, 나머지는 그 좌우로 하나씩 놓기
"""
