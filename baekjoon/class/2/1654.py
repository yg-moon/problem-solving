# 랜선 자르기
K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
left, right = 1, max(cables)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    # 현재 mid 값으로 만들 수 있는 최대 cnt를 구함
    for cable in cables:
        cnt += cable // mid
        # cnt가 N이상이라면 반복문을 조기에 종료
        if cnt >= N:
            break
    # 아직 여유가 남으면 정답을 저장하고 최소범위를 올림
    if cnt >= N:
        answer = mid
        left = mid + 1
    # 아니면 최대범위를 내림
    else:
        right = mid - 1

print(answer)

"""
- 난이도: 실버2
- 분류: 이분탐색

요약
- 이분탐색 대상: 랜선의 길이
- 범위조정 기준: 랜선의 개수
"""
