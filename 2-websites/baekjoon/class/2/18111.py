# 마인크래프트
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

min_time = int(1e9)
max_level = -1


def flatten(level):
    time = 0
    inven = B
    is_possible = True
    for i in range(N):
        for j in range(M):
            if ground[i][j] > level:
                diff = ground[i][j] - level
                inven += diff
                time += 2 * diff
            elif ground[i][j] < level:
                diff = level - ground[i][j]
                inven -= diff
                time += diff
            # 최소시간을 초과하면 반복문을 조기에 종료
            if time > min_time:
                is_possible = False
                return [time, is_possible]
    # 최종 인벤토리가 음수면 현재 높이로는 다질수 없음
    if inven < 0:
        is_possible = False
    return [time, is_possible]


for level in reversed(range(257)):
    time, is_possible = flatten(level)
    if is_possible and time < min_time:
        min_time = time
        max_level = level

print(min_time, max_level)

"""
- 난이도: 실버2
- 분류: 브루트포스

요약
- 땅의 높이를 동일하게 만드는 작업을 256부터 0까지 역순으로 시도 (복수정답 우선순위 때문)
- 일단 작업해보고, 인벤토리가 모자란지 확인하기

디버깅: 시간초과
- 이유: 배열을 2번 돌면 안됨
- 해결: 1-pass로 한번에 처리
"""
