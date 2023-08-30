# 부등호
# 출처: https://great-park.tistory.com/38
k = int(input())
signs = input().split()

min_str = ""
max_str = ""
visited = [0] * 10


def check(num1, num2, sign):
    if sign == "<":
        return num1 < num2
    else:
        return num1 > num2


def solve(depth, cur_str):
    global max_str, min_str

    if depth == k + 1:
        # 처음 생성되었으면 최소값이 들어감
        if len(min_str) == 0:
            min_str = cur_str
        # 계속 대입하다가 마지막에는 최대값이 들어감
        else:
            max_str = cur_str
        return

    # 조건을 만족하는 결과만 재귀적으로 생성
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(cur_str[-1], str(i), signs[depth - 1]):
                visited[i] = True
                solve(depth + 1, cur_str + str(i))
                visited[i] = False


solve(0, "")

print(max_str)
print(min_str)

"""
- 난이도: 실버1
- 분류: 브루트포스

- 순열 라이브러리를 사용하지 않고 구현
"""
