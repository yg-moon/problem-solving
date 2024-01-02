# 트리
def dfs(idx, arr):
    arr[idx] = -2  # 트리에서 제외시키기
    for i in range(len(arr)):
        if idx == arr[i]:
            dfs(i, arr)  # 재귀적으로 자손노드 삭제


N = int(input())
arr = list(map(int, input().split()))
erase = int(input())
answer = 0

dfs(erase, arr)

# 리프노드 개수 (깔끔하게 계산)
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        answer += 1

print(answer)

"""
- DFS 풀이 (훨씬 깔끔)

- 출처: https://wiselog.tistory.com/118
"""
