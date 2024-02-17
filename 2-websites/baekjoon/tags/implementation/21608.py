# 상어 초등학교
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N**2)]

graph = [[0] * N for _ in range(N)]
dic = dict()  # {학생 번호: [좋아하는 학생들]}

# 주의: 인접한 칸은 상하좌우 (8방향이 아님)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 학생의 자리 정하기
for num, *likes in arr:
    dic[num] = likes
    possible_pos = []

    # 각 칸에 대해 좋아하는 학생 수, 빈칸의 수 계산
    for x in range(N):
        for y in range(N):
            like_cnt = 0
            empty_cnt = 0
            if graph[x][y] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] in likes:
                            like_cnt += 1
                        elif graph[nx][ny] == 0:
                            empty_cnt += 1
                possible_pos.append((like_cnt, empty_cnt, x, y))

    # 핵심: 기준에 따라 정렬
    possible_pos.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    x = possible_pos[0][2]
    y = possible_pos[0][3]
    graph[x][y] = num

# 만족도 계산
answer = 0
score = [0, 1, 10, 100, 1000]  # 주의: i=3 값을 100이 아닌 10으로 썼음

for x in range(N):
    for y in range(N):
        cur = graph[x][y]
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] in dic[cur]:
                cnt += 1
        answer += score[cnt]

print(answer)

"""
- 난이도: 골드5
- 분류: 시뮬레이션
- 소요 시간: 40분

요약
- 시키는대로 구현하는 문제
- 위치선정: 가능한 위치를 모으고, 기준에 따라 정렬하고, 맨앞을 선택
- 좋아하는 학생 수: 해시맵
"""
