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
- 분류: 브루트포스, 백트래킹

풀이
- 순열 라이브러리 사용
- 0~9로 이루어진 길이 k+1 자리 순열을 만든다.
- 주어진 부등호를 만족하는 것중 최소와 최대를 찾는다.
"""
