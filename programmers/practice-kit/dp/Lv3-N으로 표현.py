def calc_set(set_x, set_y):
    new_set = set()
    for x in set_x:
        for y in set_y:
            new_set.add(x + y)
            new_set.add(x - y)
            new_set.add(x * y)
            if y != 0:
                new_set.add(x // y)
    return new_set


def solution(N, number):
    dp = [{} for _ in range(9)]

    dp[1] = {N}
    if number == N:
        return 1

    for i in range(2, 9):
        dp[i] = {int(str(N) * i)}
        for j in range(1, i):
            dp[i].update(calc_set(dp[j], dp[i - j]))
            if number in dp[i]:
                return i

    return -1


"""
- 요약: dp[i]: n을 i번 사용하여 만들 수 있는 모든 결과의 집합
- 구현
    - 일단 dp[i]는 i의 개수만큼 n으로 채운다. (ex. dp[2] = {55}, dp[3] = {555})
    - dp[i]에서 2~8을 다음의 로직으로 채운다:
        - dp[2]: (1,1) 에서 나올 수 있는 모든 결과를 추가
        - dp[3]: (1,2), (2,1) 에서 나올 수 있는 모든 결과를 추가
        - dp[4]: (1,3), (2,2) (3,1) 에서 나올 수 있는 모든 결과를 추가
        - …
        - 매번 결과를 확인하며 목표값이 현재 집합에 있으면 i를 리턴, 8까지 했는데 없으면 -1.
"""
