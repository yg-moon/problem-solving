# 회의실 배정
import sys

input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 핵심1: 모든 회의를 (끝나는 시간, 시작시간)의 순서로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 핵심2: 앞에서부터 돌면서, (이전 회의가 끝난시간 <= 현재 회의 시작시간)이면 cnt += 1.
cnt = 0
last_end = -1
for start, end in meetings:
    if last_end <= start:
        cnt += 1
        last_end = end

print(cnt)

"""
- 난이도: 실버1
- 분류: 그리디

디버깅
- 처음엔 회의의 지속시간이 짧은 순으로 우선순위 큐를 사용했는데, 그런식으로 푸는 문제가 아니었다.
"""
