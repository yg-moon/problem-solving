# 종이의 개수
from collections import defaultdict

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dic = defaultdict(int)


def solve(x, y, n):
    num = mat[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 핵심: 처음 숫자랑 다른게 나오는 순간 9분할로 재귀
            if mat[i][j] != num:
                third = n // 3
                # 팁: 반복되는 재귀 구문은 깔끔하게 처리
                for k in range(3):
                    for l in range(3):
                        solve(x + (k * third), y + (l * third), third)
                return
    dic[num] += 1


solve(0, 0, N)

print(dic[-1])
print(dic[0])
print(dic[1])

"""
- 난이도: 실버2
- 분류: 분할정복
"""
