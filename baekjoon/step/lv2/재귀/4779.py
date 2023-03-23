# 칸토어 집합
def erase_mid(s, l, r):
    third = (r - l) // 3
    # 재귀 종료조건
    if third == 0:
        return
    # 1. 왼쪽 뭉치에서 재귀
    erase_mid(s, l, l + third)
    # 2. 중간 뭉치를 공백으로 대체
    for i in range(l + third, l + third * 2):
        s[i] = " "
    # 3. 오른쪽 뭉치에서 재귀
    erase_mid(s, l + third * 2, r)


def cantor(n):
    s = list("-" * 3**n)
    erase_mid(s, 0, 3**n)
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
