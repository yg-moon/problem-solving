# 1학년
from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))

cur_dic = defaultdict(int)
cur_dic[arr[0]] += 1

for a in arr[1:-1]:
    nxt_dic = defaultdict(int)
    for key in cur_dic:
        cnt = cur_dic[key]
        if cnt != 0:
            if 0 <= key + a <= 20:
                nxt_dic[key + a] += cnt
            if 0 <= key - a <= 20:
                nxt_dic[key - a] += cnt
    cur_dic = nxt_dic

print(cur_dic[arr[-1]])

"""
- 난이도: 골드
- 분류: dp
- 소요 시간: 30분

- 요약: 해시맵을 통해 값과 개수를 관리하는 풀이
"""
