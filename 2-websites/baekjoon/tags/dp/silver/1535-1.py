# 안녕
N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

answer = 0


def dfs(idx, health, joy):
    global answer

    if health <= 0:
        return

    if idx >= N:
        answer = max(answer, joy)
        return

    # 1. 현재 사람 고려
    dfs(idx + 1, health - L[idx], joy + J[idx])

    # 2. 현재 사람 건너뛰기
    dfs(idx + 1, health, joy)


dfs(0, 100, 0)
print(answer)

"""
- 난이도: 실버2
- 분류: 브루트포스, dp

요약
- N이 작아서 브루트포스가 가능한 문제
- dp로 풀면 배낭 풀이를 써야하는 문제

디버깅: 틀렸습니다
- 이유: 그리디하게 풀면 반례가 생겨서 모든 경우를 고려하는 방식으로 풀어야 함
"""
