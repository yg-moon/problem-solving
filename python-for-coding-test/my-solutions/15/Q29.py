# BOJ 2110
# from 이코테
# 요약
# 가장 인접한 두 공유기 사이의 거리(gap)의 최댓값을 찾는 문제로 생각.
# 이진탐색으로 gap 값을 선정하고, 매번 공유기 설치를 시뮬레이션해서 결과에 따라 탐색범위 조정.

N, C = list(map(int, input().split()))
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

left = 1  # 이진탐색 시작범위 초기화: 가능한 최소 거리(min gap)
right = houses[N - 1] - houses[0]  # 이진탐색 끝범위 초기화: 가능한 최대 거리(max gap)
max_gap = 0

while left <= right:
    curr_gap = (left + right) // 2
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    val = houses[0]
    cnt = 1
    # curr_gap 기준으로 앞에서부터 공유기 설치해보기
    for i in range(1, N):
        if houses[i] >= val + curr_gap:
            val = houses[i]
            cnt += 1
    # C개 이상의 공유기를 설치할 수 있는 경우, 범위 증가
    if cnt >= C:
        left = curr_gap + 1
        max_gap = curr_gap  # 현재 결과를 저장
    # C개 이상의 공유기를 설치할 수 없는 경우, 범위 감소
    else:
        right = curr_gap - 1

print(max_gap)
