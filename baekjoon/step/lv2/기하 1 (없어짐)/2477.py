# 참외밭
from collections import defaultdict

K = int(input())
farm = []
cnt_dic = defaultdict(int)

for _ in range(6):
    dir, length = map(int, input().split())
    farm.append((dir, length))
    cnt_dic[dir] += 1  # 해당 방향이 몇번 등장했는지 카운트

# 전체 넓이: 방향이 1번 등장한 것끼리 곱함
total = 1
for dir, length in farm:
    if cnt_dic[dir] == 1:
        total *= length

# 뺄 넓이: 방향이 2번 등장한 것중에, 연속된 4개중 가운데 2개를 곱함
sub = 1
for i in range(len(farm)):
    if (
        cnt_dic[farm[i][0]] == 2
        and cnt_dic[farm[(i - 1) % 6][0]] == 1
        and cnt_dic[farm[(i - 2) % 6][0]] == 1
    ):
        sub *= farm[(i + 1) % 6][1] * farm[(i + 2) % 6][1]
        break

print(K * (total - sub))

"""
- 난이도: 실버2
- 분류: 기하
"""
