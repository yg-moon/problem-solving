# 과일 탕후루
from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))

dic = defaultdict(int)
l = 0
answer = 0

for r in range(N):
    dic[arr[r]] += 1

    while len(dic) > 2:
        dic[arr[l]] -= 1
        if dic[arr[l]] == 0:
            del dic[arr[l]]
        l += 1

    answer = max(answer, r - l + 1)

print(answer)

"""
- 난이도: 실버2
- 분류: 투포인터, 슬라이딩 윈도우

요약
- 슬라이딩 윈도우의 대표적인 문제
- r로 윈도우를 확장하면서, 조건을 만족할 때까지 l로 윈도우를 축소
"""
