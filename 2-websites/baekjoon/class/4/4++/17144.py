# 미세먼지 안녕!
from copy import deepcopy

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
new_graph = deepcopy(graph)


# 첫번째 공기청정기의 x좌표 찾기
def find():
    for x in range(R):
        for y in range(C):
            if graph[x][y] == -1:
                return x


cleaner = find()


# 미세먼지 확산
def spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(R):
        for y in range(C):
            if graph[x][y] > 0:
                amount = graph[x][y] // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        new_graph[nx][ny] += amount
                        new_graph[x][y] -= amount


# 공기청정기 작동
def clean(x, y, dx, dy, x_start, x_end):
    dir = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x_start <= nx <= x_end and 0 <= ny < C:
            if graph[x][y] == -1:
                new_graph[nx][ny] = 0
            elif graph[nx][ny] != -1:
                new_graph[nx][ny] = graph[x][y]
            x, y = nx, ny
        else:
            if dir == 3:
                break
            dir += 1


# T초 동안 시뮬레이션
for _ in range(T):
    spread()
    graph = deepcopy(new_graph)

    # 위쪽 공기청정기
    clean(0, 0, [1, 0, -1, 0], [0, 1, 0, -1], 0, cleaner)
    graph = deepcopy(new_graph)

    # 아래쪽 공기청정기
    clean(cleaner + 1, 0, [0, 1, 0, -1], [1, 0, -1, 0], cleaner + 1, R - 1)
    graph = deepcopy(new_graph)

# 미세먼지의 합
answer = 2
for row in graph:
    answer += sum(row)
print(answer)

"""
- 난이도: 골드4
- 분류: 구현, 시뮬레이션

다른 풀이: https://kyun2da.github.io/2021/04/20/brownsmog/
- spread()에서 내부에 임시 그래프를 만들어 최종 그래프에 값을 더하는 방식으로 구현하면
    - new_graph가 필요없다는 장점이 있지만, 결국 실행시간은 deepcopy와 똑같다.
    - 그냥 이런 방법도 있다는 것 정도.
- clean()에서 시작점을 공기청정기의 한칸 우측으로 잡으면
    - 범위 체크에서 x_end를 확인할 필요없이, R,C 이내인지만 보면 된다. (단순히 4번만 꺾으면 되므로)
    - 종료 조건도 꺾인 횟수를 확인할 필요없이, 출발점으로 되돌아왔을때 종료하면 된다.
- clean()에서 prev값을 두고 swap하는 방식으로 바람불기를 구현하면
    - 현재 그래프에서 모든걸 해결할 수 있어서 T*2번의 deepcopy를 아낄 수 있다.
    - 결과: 1100ms -> 380ms 로 실행시간이 단축된다.
"""
