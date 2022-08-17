# 같은 풀이지만, 책 구현이 더 깔끔.
N = int(input())
plans = input().split()


def valid(i, j):
    if i < 1 or j < 1 or i > N or j > N:
        return False
    return True


i = 1
j = 1

for p in plans:
    if p == "L":
        if valid(i, j - 1):
            j -= 1
    elif p == "R":
        if valid(i, j + 1):
            j += 1
    elif p == "U":
        if valid(i - 1, j):
            i -= 1
    elif p == "D":
        if valid(i + 1, j):
            i += 1

print(i, j)
