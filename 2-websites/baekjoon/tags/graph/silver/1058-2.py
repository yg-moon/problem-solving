N = int(input())
graph = [list(input()) for _ in range(N)]

connected = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                connected[i][j] = 1

answer = 0
for row in connected:
    answer = max(answer, sum(row))
print(answer)

"""
플로이드 워셜 풀이
- 모든쌍 최단거리를 찾을 때
- 중간에 거쳐가는 경로를 찾을 때
- O(N^3)이므로 입력 크기가 작을 때

참고
- https://v3.leedo.me/devs/53
"""
