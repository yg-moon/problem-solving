# 인간-컴퓨터 상호작용
from collections import defaultdict
import sys

input = sys.stdin.readline

S = input().rstrip()

# 알파벳별 구간합 배열 구하기
dic = defaultdict(list)
for i in range(ord("a"), ord("z") + 1):
    alp = chr(i)
    dic[alp].append(0)  # 팁: 첫 원소는 0으로 채우기 (L-1에 접근하므로)
    csum = 0
    for char in S:
        if alp == char:
            csum += 1
        dic[alp].append(csum)

q = int(input())

for _ in range(q):
    ch, l, r = input().split()
    l = int(l) + 1  # 팁: 구간합은 1-idx 기준
    r = int(r) + 1
    print(dic[ch][r] - dic[ch][l - 1])

"""
- 난이도: 실버1
- 분류: 누적합
"""
