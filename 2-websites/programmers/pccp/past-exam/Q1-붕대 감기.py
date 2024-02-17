from collections import deque


def solution(bandage, health, attacks):
    t, x, y = bandage
    attacks = deque(attacks)
    max_health = health

    cur_health = health
    streak = 0
    time = 0

    while attacks:
        # 공격을 받은 경우
        if time == attacks[0][0]:
            attack_time, damage = attacks.popleft()
            cur_health -= damage
            if cur_health <= 0:
                return -1
            streak = 0
        # 공격을 받지 않은 경우
        else:
            cur_health = min(max_health, cur_health + x)
            streak += 1
            if streak == t:
                cur_health = min(max_health, cur_health + y)
                streak = 0
        time += 1

    return cur_health


"""
- 난이도: Lv1
- 분류: 시뮬레이션
- 소요 시간: 15분

요약
- 일단 매초마다 체력을 회복 (최대치 이상 불가, 연속은 쌓임)
- 공격이 있는 시간인지 확인하고 반영 (0 이하시 사망, 연속은 초기화)
- 효율성: 공격 정보를 큐로 관리하고 맨앞의 시간을 확인
"""
