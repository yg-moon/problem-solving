# 마인크래프트
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
min_time = int(1e9)
max_level = -1

for level in reversed(range(257)):
    time = 0
    inven = B
    is_possible = True

    def flatten():
        global time, inven, is_possible
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
                    return
        # 최종 인벤토리가 음수면 현재 높이로는 다질수 없음
        if inven < 0:
            is_possible = False
            return

    flatten()

    if is_possible and time < min_time:
        min_time = time
        max_level = level

print(min_time, max_level)

"""
- 난이도: 실버2
- 분류: 브루트포스

조건
- 목표: 최소시간. (여러개일 경우, 땅의 높이가 높은 것)
- 블록 제거: 2초, 블록 놓기: 1초.
- 블록 놓는건 인벤토리 안에 있는 만큼만 가능.

아이디어
- 땅의 높이가 높은 쪽부터 탐색.
- 인벤토리가 부족하면 땅을 깎아서 보충해야 함.

디버깅
- 접근: 이분탐색으로는 풀 수 없다. (지나쳐버린 범위에도 정답의 가능성이 존재하기 때문)
- 실수: 블록 1개 제거에 2초이므로, n개 제거시 2*n 초가 걸림.
- 시간초과: 배열을 2번 돌면 안된다. 1-pass로 한번에 처리해야 한다.
"""
