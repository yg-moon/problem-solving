# 빵집
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

pipe = [[0] * C for _ in range(R)]
answer = 0


def dfs(x, y):
    global answer

    # 들어오면서 파이프를 짓기
    pipe[x][y] = 1

    if y == C - 1:
        answer += 1
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == "." and pipe[nx][ny] == 0:
            # 정답이 발견되면 즉시 종료하며 그 사실을 전달
            if dfs(nx, ny):
                return True

    return False


for i in range(R):
    dfs(i, 0)

print(answer)

"""
- 난이도: 골드2
- 분류: DFS, 그리디
- 소요 시간: 50분 (풀이 20분, 디버깅 30분)

요약
- DFS로 매번 '오른쪽 위, 오른쪽, 오른쪽 아래' 순서로 짓기
- 정답이 발견되면 즉시 종료하며 그 사실을 전달

디버깅: 시간초과
- 원인1: 방문한 경로를 list로 저장했던 것이 문제였음
    - 해결: 들어오면서 파이프를 짓고, 나가면서 지우는 가벼운 연산으로 변경
- 원인2: 나가면서 지우는 과정을 없애야 함
    - 이유: 어차피 다른 경로로 이 자리에 와도 실패할 것이기 때문에, 일종의 방문표시
"""
