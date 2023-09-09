# 연산자 끼워넣기
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

INF = int(1e9)
min_val = INF
max_val = -INF


def dfs(i, res):
    # i: 배열 인덱스 겸 연산횟수
    # res: 현재까지의 결과
    global add, sub, mul, div, min_val, max_val
    if i == N:
        min_val = min(min_val, res)
        max_val = max(max_val, res)
        return

    if add > 0:
        add -= 1
        dfs(i + 1, res + nums[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, res - nums[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, res * nums[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, int(res / nums[i]))  # 이렇게 하면 C++14 기준을 따름
        div += 1


dfs(1, nums[0])

print(max_val)
print(min_val)

"""
- 난이도: 실버1
- 분류: 백트래킹

- 핵심: 배열을 전부 들고 재귀하는게 아니라, 상태정보만 가진 상태로 진행한다.
"""
