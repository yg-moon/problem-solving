def solution(n, computers):
    answer = 0
    visited = set()

    def dfs(i):
        visited.add(i)
        for j in range(n):
            if i != j and computers[i][j] == 1 and j not in visited:
                dfs(j)

    for node in range(n):
        if node not in visited:
            dfs(node)
            answer += 1

    return answer


"""
- 요약: DFS 섬 만들기
    - 모든 노드에 dfs를 해보고, 네트워크 하나가 끝날때마다 카운트 +1.
    - 이미 방문한 노드일 경우 dfs를 시작하지 않고 스킵.
"""
