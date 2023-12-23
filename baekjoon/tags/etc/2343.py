# 기타 레슨
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 파라메트릭 서치
# - 대상: 블루레이 크기
# - 기준: 블루레이 개수

# 주의: 초기값 설정
l = max(arr)  # 최대 단일강의의 크기 (일단 시디에 담겨야 하므로)
r = sum(arr)  # 전체 강의를 한번에 담았을 때의 크기
answer = l  # 가능한 최소는 0이 아니라 l

while l <= r:
    mid = (l + r) // 2
    cur_sum = 0
    cnt = 0

    for a in arr:
        if cur_sum + a > mid:
            cur_sum = 0
            cnt += 1
        cur_sum += a
        # 조기종료
        if cnt > M:
            break

    if cur_sum != 0:
        cnt += 1

    # 개수가 너무 많으면, 크기를 늘려보기
    if cnt > M:
        l = mid + 1
    # 답이 가능하면 저장하고, 최대한 더 줄여보기
    else:
        answer = mid
        r = mid - 1

print(answer)

"""
- 난이도: 실버1
- 분류: 이분탐색

- 핵심: 파라메트릭 서치
- 디버깅: 초기값을 잘못 두었음 
"""
