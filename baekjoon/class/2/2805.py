# 나무 자르기
N, M = map(int, (input().split()))
trees = list(map(int, input().split()))
left, right = 0, max(trees) - 1
answer = 0

while left <= right:
    mid = (left + right) // 2
    take_home = 0
    # 현재 mid 값으로 만들 수 있는 최대 take_home을 구함
    for tree in trees:
        diff = tree - mid
        if diff > 0:
            take_home += diff
        # take_home이 M 이상이라면 반복문을 조기에 종료
        if take_home >= M:
            break
    # 아직 여유가 남으면 정답을 저장하고 최소범위를 올림
    if take_home >= M:
        answer = mid
        left = mid + 1
    # 아니면 최대범위를 내림
    else:
        right = mid - 1

print(answer)

"""
- 난이도: 실버2
- 분류: 이분 탐색

요약
- 이분탐색 대상: 절단기의 높이
- 범위조정 기준: 집에 가져가는 나무의 높이
"""
