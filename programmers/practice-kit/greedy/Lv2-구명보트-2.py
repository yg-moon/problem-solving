def solution(people, limit):
    people.sort()
    boat = 0
    l, r = 0, len(people) - 1

    while l < r:
        # 매번 가장 가벼운 사람과 가장 무거운 사람을 한명씩 태워보냄
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
            boat += 1
        # 몸무게의 합이 제한을 초과하면 일단 무거운 사람만 태워보냄
        else:
            r -= 1
            boat += 1

    # 마지막에 한명이 남은 경우 처리
    if l == r:
        boat += 1

    return boat


"""
- 투포인터 풀이
"""
