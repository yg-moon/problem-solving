# 생태학
from collections import defaultdict
import sys

input = sys.stdin.readline

dic = defaultdict(int)
N = 0

while True:
    tree = input().strip()  # 주의: sys로 받고 문자열 일때는 필요
    if not tree:  # 팁: try-except 없이 해결
        break
    dic[tree] += 1
    N += 1

for tree in sorted(dic.keys()):
    print(f"{tree} {dic[tree] / N * 100:.4f}")  # 주의: round로 하면 틀림

"""
- 난이도: 실버2
- 분류: 해시
"""
