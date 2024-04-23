def calc_diff(apeach, ryan):
    apeach_score = 0
    ryan_score = 0

    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue
        if apeach[i] >= ryan[i]:
            apeach_score += 10 - i
        else:
            ryan_score += 10 - i

    return ryan_score - apeach_score


# a가 더 좋은 순서일 경우 True
def compare(a, b):
    return a[::-1] > b[::-1]


def solution(n, info):
    ryan_init = [0] * 11
    max_diff = 0
    answer = []

    def dfs(idx, arrow, ryan):
        nonlocal max_diff, answer

        if arrow == 0:
            diff = calc_diff(info, ryan)
            # 주의: 분기조건 제대로 구분하기
            if diff > max_diff or (diff == max_diff and compare(ryan, answer)):
                max_diff = diff
                answer = ryan[:]
            return

        if idx > 10:
            return

        # 1. 화살을 쏘지 않는 경우
        dfs(idx + 1, arrow, ryan)

        # 2. 화살을 한발만 더 맞추는 경우
        apeach = info[idx] + 1
        if arrow >= apeach:
            ryan[idx] = apeach
            dfs(idx + 1, arrow - apeach, ryan)
            ryan[idx] = 0

        # 남은 화살은 0점에 몰아주기
        if idx == 10:
            ryan[idx] = arrow
            dfs(idx + 1, 0, ryan)
            ryan[idx] = 0

    dfs(0, n, ryan_init)

    if max_diff == 0:
        return [-1]
    else:
        return answer


"""
- 분류: 백트래킹
- 소요 시간: 45분

조건
- k점을 여러 발 맞혀도 k점만 가져감
- 개수가 같으면 어피치의 점수가 됨
- 아무도 못 맞췄으면 0점이 됨
- 가장 큰 점수 차이로 우승하면서, 가장 낮은 점수를 더 많이 맞힌 경우가 정답

요약
- 점수 계산하는 함수 만들기
- 백트래킹으로 돌면서, 화살을 0~남은개수 만큼 쏴보기
- 남은 화살의 개수가 0이 되었을때 점수 계산

핵심
- 가장 낮은 점수를 더 많이 맞힌 경우를 고르기
    - 목표: 뒤에 숫자가 높아지는게 나중에 나와야 함
    - 방법: 비교 함수를 만들어서 해결 (굳이 탐색 순서로 해결하려고 하지 말자)

해설
- 탐색 횟수 줄이기
    - 어피치보다 1발 더 맞추거나, 아예 맞추지 않는 경우로만 구분
    - 남은 화살은 0점에 몰아주기
"""
