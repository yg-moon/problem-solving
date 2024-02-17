# 부분수열의 합
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


def dfs(i, cur_sum):
    global cnt

    if i >= N:
        return

    cur_sum += arr[i]

    if cur_sum == S:
        cnt += 1

    dfs(i + 1, cur_sum)  # 1. 현재 수를 선택한 경우
    dfs(i + 1, cur_sum - arr[i])  # 2. 현재 수를 선택하지 않은 경우


dfs(0, 0)

print(cnt)

"""
- 난이도: 실버2
- 분류: 백트래킹

- 요약: 앞에서부터 모든 경우를 탐색해나가기
- 주의: 부분 수열 != 연속된 부분 수열
"""
