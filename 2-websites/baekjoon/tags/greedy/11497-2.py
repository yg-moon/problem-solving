T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    max_diff = 0
    for i in range(2, N):
        max_diff = max(max_diff, abs(arr[i] - arr[i - 2]))

    print(max_diff)

"""
개선
- 직접 배열을 만들지 않고도 해결
- 1번과 3번의 높이차, 2번과 4번의 높이차, ... n-2번과 n번의 높이차

참고
- https://velog.io/@ready2start/Python-백준-11497-통나무-건너뛰기
"""
