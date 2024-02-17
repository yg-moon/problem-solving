# 스타트와 링크
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_diff = int(1e9)


def get_stats(team):
    res = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            # 주의: 여기서 i,j가 아니라 team[i], team[j]를 넣어야 함
            res += arr[team[i]][team[j]]
            res += arr[team[j]][team[i]]
    return res


def solve(start, team):
    global min_diff

    if len(team) == N // 2:
        other_team = [i for i in range(N) if i not in team]
        min_diff = min(min_diff, abs(get_stats(team) - get_stats(other_team)))
        return

    for i in range(start, N):
        if i not in team:
            team.append(i)
            solve(i + 1, team)
            team.pop()


solve(0, [])

print(min_diff)

"""
- 난이도: 실버2
- 분류: 백트래킹
"""
