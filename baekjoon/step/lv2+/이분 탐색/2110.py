# 공유기 설치
# 출처: 이코테
N, C = list(map(int, input().split(" ")))
arr = sorted([int(input()) for _ in range(N)])

start = 1  # min gap
end = arr[-1] - arr[0]  # max gap
answer = 0

while start <= end:
    mid = (start + end) // 2
    # 첫째 집에는 무조건 공유기를 설치한다고 가정하고, 앞에서부터 가능한데까지 하나씩 설치
    val = arr[0]
    cnt = 1
    for i in range(1, N):
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1

    # 여유가 있으면, 현재 결과를 저장하고 범위를 올리기
    if cnt >= C:
        answer = mid
        start = mid + 1
    # 아니면 범위를 줄이기
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
