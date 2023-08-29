result = []


# 전통적인 방식
def permute_1(arr, path, visited):
    if len(path) == len(arr):
        result.append(path[:])  # 주의: 복사본을 붙여야 함
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            permute_1(arr, path, visited)
            path.pop()
            visited[i] = False


# 효율적인 스왑 방식
def permute_2(arr):
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    backtrack(0)


# 비효율적이지만 가능한 방식
def permute_3(arr, path):
    if not arr:
        result.append(path)
        return
    for i in range(len(arr)):
        permute_3(arr[:i] + arr[i + 1 :], path + [arr[i]])


# 예제 실행
arr = [1, 2, 3]

permute_1(arr, [], [False] * len(arr))
print(result)
result.clear()

permute_2(arr)
print(result)
result.clear()

permute_3(arr, [])
print(result)
result.clear()
