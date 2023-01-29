# 좌표 압축
N = int(input())
arr = list(map(int, input().split()))

dic = {}
for i, a in enumerate(sorted(set(arr))):
    dic[a] = i

answer = []
for a in arr:
    answer.append(dic[a])

print(*answer)

"""
- 난이도: 실버2
- 분류: 좌표압축

디버깅
- list.index()는 O(n) 이라서 시간초과가 나서 dict를 써야했다.
"""
