# 누울 자리를 찾아라
# 출처: https://my-coding-notes.tistory.com/525
N = int(input())
arr = [list(input()) for _ in range(N)]

row = 0
col = 0

for i in range(N):
    row_tmp = 0
    col_tmp = 0
    for j in range(N):
        # row
        if arr[i][j] == ".":
            row_tmp += 1
        else:
            row_tmp = 0
        # 핵심: 단순히 tmp==2 되면 정답+=1 하면 됨
        if row_tmp == 2:
            row += 1

        # col
        if arr[j][i] == ".":
            col_tmp += 1
        else:
            col_tmp = 0
        if col_tmp == 2:
            col += 1

print(row, col)

"""
- 난이도: 실버5
- 분류: 문자열, 구현

- 그냥 풀어도 되는 문제
"""
