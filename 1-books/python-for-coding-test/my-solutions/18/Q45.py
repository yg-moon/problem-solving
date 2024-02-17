# BOJ 3665
# 출처: 이코테
from collections import deque

TC = int(input())
for _ in range(TC):
    N = int(input())
    indegree = [0] * (N + 1)
    graph = [[False] * (N + 1) for _ in range(N + 1)]

    # 작년 순위
    data = list(map(int, input().split()))
    # 간선 정보 입력: 자신보다 등수가 낮은 팀들을 전부 가리키도록
    for i in range(N):
        for j in range(i + 1, N):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 상대적 순위의 변경: 해당 간선의 방향을 반대로 변경
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        # 작년에는 a가 b보다 높았던 경우
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬
    result = []
    Q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            Q.append(i)

    unique = True
    cycle = False

    # 노드의 개수만큼 반복
    for _ in range(N):
        # N개의 노드를 방문하기 전에 큐가 비어 있다면: 사이클이 발생했다는 의미
        if len(Q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면: 가능한 정렬 결과가 여러 개라는 의미
        if len(Q) >= 2:
            unique = False
            break
        # 큐에서 원소를 꺼내기
        # 그 순서가 위상정렬 순서
        curr = Q.popleft()
        result.append(curr)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, N + 1):
            if graph[curr][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    Q.append(j)

    # 결과 출력
    if cycle:
        print("IMPOSSIBLE")
    elif not unique:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
