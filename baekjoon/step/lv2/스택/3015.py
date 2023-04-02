# 오아시스 재결합
# 출처: https://velog.io/@minayeah/Python-백준-3015-오아시스-재결합
# 설명: https://0902.tistory.com/57
import sys

input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]

stack = []  # (키, 같은 키 cnt)
answer = 0

for h in heights:
    # 1. 뽑을거 뽑기
    # 기본: 스택top이 현재 사람보다 키가 작다면: while로 pop하며 계산
    # 주의: 정답에 '같은 키 cnt'를 더해야 함
    while stack and stack[-1][0] < h:
        answer += stack.pop()[1]

    # 현재 스택은 내림차순으로 정렬된 상태
    # 2. 현재 사람 추가하기
    # 2-1. 스택이 비었으면: 현재 사람을 추가
    if not stack:
        stack.append((h, 1))

    # 2-2. 스택top이 현재 사람과 키가 같다면:
    elif stack[-1][0] == h:
        # 현재 사람을 뽑고, 키의 cnt를 정답에 추가
        cnt = stack.pop()[1]
        answer += cnt
        # 스택이 비지 않았다면: 정답+1 (남은 top과 현재 사람이 마주볼 수 있으므로)
        if stack:
            answer += 1
        # 키의 cnt를 +1 해서 현재 사람을 추가
        stack.append((h, cnt + 1))

    # 2-3. 스택top이 현재 사람보다 키가 크다면: 정답+1 하고 현재 사람을 추가
    elif stack[-1][0] > h:
        answer += 1
        stack.append((h, 1))

print(answer)

"""
- 난이도: 플래5
- 분류: 스택

핵심
- 같은 키 cnt를 관리
- 경우의 수를 잘 나누어 로직을 설계
"""
