# 부등호
import sys
from itertools import permutations

k = int(input())
signs = input().split()

nums = list(range(10))
min_str = str(sys.maxsize)
max_str = str(-sys.maxsize)

for perm in permutations(nums, k + 1):
    correct = True
    for i in range(k):
        if signs[i] == "<" and perm[i] >= perm[i + 1]:
            correct = False
            break
        elif signs[i] == ">" and perm[i] <= perm[i + 1]:
            correct = False
            break
    if correct:
        perm_str = "".join([str(x) for x in perm])
        if int(min_str) > int(perm_str):
            min_str = perm_str
        if int(max_str) < int(perm_str):
            max_str = perm_str

print(max_str)
print(min_str)

"""
- 난이도: 실버1
- 분류: 브루트포스

- 모든 순열을 생성하고 그중에서 찾는다.
"""
