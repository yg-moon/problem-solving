# 재귀의 귀재
def is_palindrome(s):
    return recur(s, 0, len(s) - 1)


def recur(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recur(s, l + 1, r - 1)


T = int(input())
for _ in range(T):
    S = input()
    cnt = 0
    print(is_palindrome(S), cnt)

"""
- 난이도: 브론즈2
- 분류: 재귀

- 재귀적으로 팰린드롬을 판별하는 방법
"""
