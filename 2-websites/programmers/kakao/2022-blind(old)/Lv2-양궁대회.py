candidates = []  # 정답 후보
max_diff = 0  # 최대 점수 차이

# 라이언이 몇 점 차이로 이겼는지 계산
def calc_diff(apeach, ryan):
    a_score = 0
    r_score = 0

    for i in range(11):
        if ryan[i] > apeach[i]:
            r_score += 10 - i
        elif ryan[i] <= apeach[i] and apeach[i] != 0:
            a_score += 10 - i

    result = r_score - a_score
    if result > 0:
        return result
    else:
        return -1  # 라이언이 진 경우


def dfs(apeach, ryan, arrow, target):
    global max_diff
    # 최대 차이면 현재 ryan 배열을 정답에 기록
    diff = calc_diff(apeach, ryan)
    if diff == max_diff and ryan not in candidates:
        candidates.append(ryan)
    # 새로운 최대 차이가 나왔을 경우, 여태까지의 기록을 비워주고, 현재 기록을 추가
    elif diff > max_diff:
        candidates.clear()
        candidates.append(ryan)
        max_diff = diff

    if target == 0:
        return

    new_ryan = ryan[:]
    next_target = target - 1
    # Case1. 현재 점수를 맞추지 않는 경우
    dfs(apeach, new_ryan, arrow, next_target)
    # Case2. 현재 점수를 맞추는 경우
    # 남은 화살이 충분할때, 현재 점수의 ryan 배열값을 올리고, arrow를 줄이기
    required_arrow = apeach[10 - target]
    if arrow >= required_arrow + 1:
        new_ryan[10 - target] = required_arrow + 1
        arrow -= required_arrow + 1
    # 다음 목표가 0인 경우 남은 화살 몰아주기
    if next_target == 0:
        new_ryan[10] = arrow
        arrow = 0
    dfs(apeach, new_ryan, arrow, next_target)


def solution(n, info):
    ryan_init = [0] * 11
    dfs(info, ryan_init, n, 10)
    candidates.sort(key=lambda x: x[::-1])
    if not candidates:
        return [-1]
    else:
        return candidates[-1]
