# 숫자고르기
N = int(input())
arr = [0] + [int(input()) for _ in range(N)]  # 1-idx
result = set()


def dfs(idx):
    visited.add(idx)
    start.add(idx)
    end.add(arr[idx])

    if arr[idx] not in visited:
        dfs(arr[idx])


for i in range(1, N + 1):
    if i not in result:
        visited = set()
        start = set()
        end = set()
        dfs(i)

    if start == end:
        result.update(start)  # 주의: set.union()은 새 리턴값을 생성

print(len(result))
for r in sorted(result):
    print(r)

"""
- 난이도: 골드5
- 분류: DFS
- 소요 시간: 30분 (풀이20분, 디버깅10분)

요약
- 핵심: 두 집합이 일치하고, 최대한 많이 뽑으려면 어떻게 해야 하는가?
- 방법: DFS로 돌면서, 이미 방문한 곳이 나오기전까지 돌고, 출발지와 도착지가 같은지 확인

디버깅: 틀렸습니다
- 원인: 결과에 중복된 값이 여러번 출력되고 있었음. set으로 처리해서 해결.
"""
