# 누울 자리를 찾아라
N = int(input())
arr = [list(input()) for _ in range(N)]

row = 0
col = 0

for i in range(N):
    splt = "".join(arr[i]).split("X")
    for s in splt:
        if len(s) >= 2:
            row += 1

for j in range(N):
    splt = "".join([arr[i][j] for i in range(N)]).split("X")
    for s in splt:
        if len(s) >= 2:
            col += 1

print(row, col)

"""
- split()을 사용한 풀이
"""
