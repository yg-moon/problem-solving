# BOJ 2110
# 출처: 이코테

N, C = list(map(int, input().split()))

houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

left = 1  # 시작범위: 가능한 최소 거리(min gap)
right = houses[N - 1] - houses[0]  # 끝범위: 가능한 최대 거리(max gap)
max_gap = 0

while left <= right:
    curr_gap = (left + right) // 2
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    curr_house = houses[0]
    cnt = 1
    # curr_gap 기준으로 앞에서부터 공유기 설치해보기
    for i in range(1, N):
        if houses[i] >= curr_house + curr_gap:
            curr_house = houses[i]
            cnt += 1
    # C개 이상의 공유기를 설치할 수 있는 경우, 범위 증가
    if cnt >= C:
        left = curr_gap + 1
        max_gap = curr_gap  # 현재 결과를 저장
    # C개 이상의 공유기를 설치할 수 없는 경우, 범위 감소
    else:
        right = curr_gap - 1

print(max_gap)
