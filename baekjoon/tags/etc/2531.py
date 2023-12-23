# 회전초밥
N, D, K, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

l = 0
r = 0
answer = 0

while l < N:
    r = l + K
    cur_set = set()
    can_use_coupon = True

    for i in range(l, r):
        i %= N  # 원형처리
        cur_set.add(arr[i])
        if arr[i] == C:  # 쿠폰처리
            can_use_coupon = False

    cnt = len(cur_set)
    if can_use_coupon:
        cnt += 1

    answer = max(answer, cnt)
    l += 1

print(answer)

"""
- 난이도: 실버1
- 분류: 브루트포스, 투포인터, 슬라이딩 윈도우

문제 해석
- 정확히 k개를 연속해서 먹는다.
- 그 안에서 중복이 있어도 상관없고, 단순히 최대 가짓수를 구한다.
- 쿠폰에 적힌 번호가 벨트 위에 없다면 요리사가 새로 만들어 제공한다. (있으면 안 제공)
- (문제 해석이 제대로 안 돼서 어려웠네)

풀이
- l은 0~N-1까지 돌며, r은 l+K로 설정
- 범위내에서 모든 원소들을 set에 넣고 개수를 세기 (주의: 원형처리, 쿠폰처리)
- 결국 브루트포스로 모든 경우를 탐색하는것

- 참고: https://velog.io/@study-dev347/백준-2531-회전-초밥
"""
