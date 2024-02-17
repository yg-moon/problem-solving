# 공유기 설치
# 출처: 이코테
N, C = list(map(int, input().split(" ")))
arr = list([int(input()) for _ in range(N)])

arr.sort()

start = 1  # min gap
end = arr[-1] - arr[0]  # max gap
answer = 0

while start <= end:
    mid = (start + end) // 2

    # 첫 집에는 무조건 설치하고, 앞에서부터 하나씩 진행
    last = arr[0]
    cnt = 1
    for i in range(1, N):
        if arr[i] - last >= mid:  # mid 이상의 거리가 되도록 설치
            cnt += 1
            last = arr[i]

    # 공유기의 개수가 충분하면 거리를 늘려봄
    if cnt >= C:
        answer = mid
        start = mid + 1
    # 공유기의 개수가 모자라면 거리를 줄여봄
    else:
        end = mid - 1

print(answer)

"""
- 난이도: 골드4
- 분류: 이분탐색

요약
- 이분탐색 대상: 가장 인접한 두 공유기 사이의 거리(gap)
- 범위조정 기준: 설치한 공유기의 개수
"""
