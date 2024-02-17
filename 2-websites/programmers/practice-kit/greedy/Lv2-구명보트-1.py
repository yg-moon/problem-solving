from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    boat = 0

    while len(people) >= 2:
        # 매번 가장 가벼운 사람과 가장 무거운 사람을 한명씩 태워보냄
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            boat += 1
        # 몸무게의 합이 제한을 초과하면 일단 무거운 사람만 태워보냄
        else:
            people.pop()
            boat += 1

    # 마지막에 한명이 남은 경우 처리
    if people:
        boat += 1

    return boat


"""
- deque 풀이
"""
