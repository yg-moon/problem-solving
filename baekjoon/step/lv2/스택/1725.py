# 히스토그램
# 출처: https://www.acmicpc.net/blog/view/12
import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

stack = []
answer = 0

for i in range(N):
    # 스택 top보다 낮은게 들어오면 while로 pop하며 계산
    while stack and arr[stack[-1]] > arr[i]:
        height = arr[stack.pop()]
        width = i
        if stack:
            width = i - stack[-1] - 1
        answer = max(answer, width * height)
    # 스택에는 인덱스만 넣음
    stack.append(i)

# 스택에 남은것들 처리
while stack:
    height = arr[stack.pop()]
    width = N
    if stack:
        width = N - stack[-1] - 1
    answer = max(answer, width * height)

print(answer)

"""
- 난이도: 플래5
- 분류: 스택

핵심
- 정답을 구하려면 모든 막대 x에 대해서, x를 높이로 하면서 만들 수 있는 가장 큰 직사각형을 찾아야 함.
- 1. 스택으로 현재보다 낮은게 나올때까지 기다리다가, pop 할 수 있는만큼만 계산.
- 2. 끝까지 스택에 남은 것들은 전체범위를 기준으로 다시 계산.
- (출처의 그림을 보면 어떤 순서로 계산이 이루어지는지 알 수 있음)
"""
