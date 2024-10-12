# 가장 긴 증가하는 부분 수열2
# 출처: https://hongcoding.tistory.com/14
# 설명: https://jainn.tistory.com/90
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

lis = [0]

for num in arr:
    # lis 배열에서 num이 들어갈 위치를 이진 탐색으로 찾기
    idx = bisect_left(lis, num)

    # 적절한 위치에 삽입, 없으면 추가
    if idx < len(lis):
        lis[idx] = num
    else:
        lis.append(num)

print(len(lis) - 1)

"""
- bisect 모듈로 더 간단하게 풀기
- O(nlogn)
"""
