# 게임
X, Y = map(int, input().split())

# 주의: 소수점에 대해 연산하지 말기 (부동소수점 오차)
Z = int((Y * 100) / X)

# 핵심1: 99부터는 오를 수 없음 & 떨어지는 것은 불가능
if Z >= 99:
    print(-1)
else:
    # 핵심2: 파라메트릭 서치
    # - 대상: 추가 게임 횟수
    # - 기준: 승률
    l = 1
    r = X
    answer = 0

    while l <= r:
        mid = (l + r) // 2
        if int((Y + mid) * 100 / (X + mid)) <= Z:
            l = mid + 1  # 주의: l+=1 로 쓰면 안됨
        else:
            answer = mid  # 일단 가능한 답을 저장하고, 더 작은 답을 찾기
            r = mid - 1

    print(answer)

"""
- 난이도: 실버3
- 분류: 이분탐색

- 참고: https://hillier.tistory.com/70
"""
