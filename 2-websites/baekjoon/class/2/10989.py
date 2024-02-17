# 수 정렬하기 3
import sys

input = sys.stdin.readline

N = int(input())

arr = [0] * 10001

for _ in range(N):
    x = int(input())
    arr[x] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)


"""
- 난이도: 브론즈1
- 분류: 정렬

기수 정렬 (Radix sort)
- 메모리 제한이 8MB 이므로, O(N)의 입력을 모두 담기에는 공간이 충분하지 않다.
- 따라서 입력값을 직접 저장하지 않고도 정렬할 수 있는 방법을 사용한다.

빠른 입출력
- 입력이 1000만번까지 반복되므로 필요하다.
"""
