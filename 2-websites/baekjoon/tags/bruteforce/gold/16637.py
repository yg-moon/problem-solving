# 괄호 추가하기
N = int(input())
s = input()
max_res = -1 * (2**31)


def calc(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2


def dfs(idx, val):
    # idx: 현재 위치
    # val: 현재까지 계산한 값
    global max_res

    # 끝에 도착했으면 최댓값 갱신
    if idx == N - 1:
        max_res = max(max_res, val)
        return

    # Case1: 맨앞부터 괄호치기
    # (ex. A @ B @ C 에서 A,B를 먼저 계산하는 경우)
    if idx + 2 < N:
        dfs(idx + 2, calc(val, s[idx + 1], int(s[idx + 2])))

    # Case2: 한칸 건너뛰고 괄호치기
    # (ex. A @ B @ C 에서 B,C를 먼저 계산하는 경우)
    if idx + 4 < N:
        dfs(
            idx + 4,
            calc(
                val,
                s[idx + 1],
                calc(int(s[idx + 2]), s[idx + 3], int(s[idx + 4])),
            ),
        )


dfs(0, int(s[0]))

print(max_res)

"""
- 난이도: 골드3
- 분류: 브루트포스, 재귀

핵심
- 가능한 경우의 수를 나열하고 재귀적으로 풀기 (Case1, Case2)
- 매번 어떤 값을 들고 진행할지 정하기 (idx, val)

- 참고: https://velog.io/@weenybeenymini/백준-16637번-괄호-추가하기
"""
