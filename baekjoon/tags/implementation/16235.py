# 나무 재테크
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 효율성: defaultdict 대신 list 사용
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)  # 주의: 주어지는 입력은 1-idx

# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

soil = [[5] * N for _ in range(N)]

for _ in range(K):
    # 모든 나무들을 정렬
    for x in range(N):
        for y in range(N):
            trees[x][y].sort()

    # 봄
    dead_trees = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new_trees = []
            for age in trees[x][y]:
                if soil[x][y] >= age:
                    soil[x][y] -= age
                    new_trees.append(age + 1)
                else:
                    dead_trees[x][y] += age // 2
            trees[x][y] = new_trees

    # 여름
    for x in range(N):
        for y in range(N):
            soil[x][y] += dead_trees[x][y]

    # 가을
    tmp_dic = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for age in trees[x][y]:
                if age % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            tmp_dic[nx][ny] += 1

    # 주의: 이렇게 따로 안하면 런타임에러 (list changed during iteration)
    for x in range(N):
        for y in range(N):
            for _ in range(tmp_dic[x][y]):
                trees[x][y].append(1)

    # 겨울
    for x in range(N):
        for y in range(N):
            soil[x][y] += A[x][y]

answer = 0
for x in range(N):
    for y in range(N):
        answer += len(trees[x][y])
print(answer)

"""
- 난이도: 골드3
- 분류: 시뮬레이션
- 소요 시간: 70분 (풀이 30분, 디버깅 40분)

요약
- 시키는대로 구현하는 문제
- 추가적인 최적화 가능 (다만, 입력 크기가 작아서 이번 문제에서는 큰 효과가 없음)
    - 1. 정렬 대신 deque 사용 (16ms)
    - 2. 한번의 반복으로 처리 (16ms)
    - 3. 빠른 입출력 (4ms)

디버깅: 시간초과
- defaultdict 대신 list를 사용

조건 정리
- 처음 모든 칸의 양분은 5
- M개의 나무를 심는데, 한 칸에 여러개 가능
- 사계절
    - 봄: 양분 먹기
    - 여름: 죽은 나무 양분 변환
    - 가을: 나무 번식
    - 겨울: 양분 추가
- 정답: K년 이후 살아있는 나무의 개수
"""
