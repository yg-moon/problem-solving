# 부등호
# 출처: https://great-park.tistory.com/38
k = int(input())
signs = input().split()

min_str = ""
max_str = ""
visited = [0] * 10


def check(num1, sign, num2):
    if sign == "<":
        return num1 < num2
    else:
        return num1 > num2


def solve(cur_str):
    global max_str, min_str

    if len(cur_str) == k + 1:
        # 처음 생성되었으면 최소값이 들어감
        if len(min_str) == 0:
            min_str = cur_str
        # 계속 대입하다가 마지막에는 최대값이 들어감
        else:
            max_str = cur_str
        return

    # 조건을 만족하는 순열만 재귀적으로 생성
    for i in range(10):
        if not visited[i]:
            if not cur_str or check(cur_str[-1], signs[len(cur_str) - 1], str(i)):
                visited[i] = True
                solve(cur_str + str(i))
                visited[i] = False


solve("")

print(max_str)
print(min_str)

"""
- 난이도: 실버1
- 분류: 백트래킹

- 백트래킹으로 조건을 만족하는 순열만 생성한다.
"""
