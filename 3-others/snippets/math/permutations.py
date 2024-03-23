result = []


def perm(arr, path, visited):
    if len(path) == len(arr):
        result.append(path[:])  # 주의: 복사본을 붙여야 함
        return
    for i in range(len(arr)):  # 앞에서 부터 돌면서 방문하지 않은것만
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            perm(arr, path, visited)
            path.pop()
            visited[i] = False


def comb(arr, path, start):
    if len(path) == len(arr):
        result.append(path[:])
        return
    for i in range(start, len(arr)):  # 시작위치를 하나씩 올려가면서
        path.append(arr[i])
        comb(arr, path, i + 1)
        path.pop()


# Test
arr = [1, 2, 3]

perm(arr, [], [False] * len(arr))
print(result)
result.clear()

comb(arr, [], 0)
print(result)
result.clear()
