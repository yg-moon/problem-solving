# 칸토어 집합
def erase(s, l, r):
    third = (r - l) // 3
    if third == 0:
        return
    # 왼쪽 뭉치에서 재귀
    erase(s, l, l + third)
    # 중간 뭉치를 공백으로 대체
    for i in range(l + third, l + third * 2):
        s[i] = " "
    # 오른쪽 뭉치에서 재귀
    erase(s, l + third * 2, r)


def cantor(n):
    s = list("-" * 3**n)
    erase(s, 0, 3**n)
    return "".join(s)


while True:
    try:
        N = int(input())
        print(cantor(N))
    except:
        break

"""
- 난이도: 실버3
- 분류: 재귀
"""
