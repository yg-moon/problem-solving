from collections import deque


def solution(coin, cards):
    N = len(cards)
    hand = set(cards[: N // 3])
    deck = deque(cards[N // 3 :])
    drawn = set()
    round = 1

    def pair_exists(set1, set2):
        nonlocal coin, round
        for x in set1:
            y = N + 1 - x
            if y in set2:
                set1.remove(x)
                set2.remove(y)
                return True
        return False

    while deck:
        drawn.add(deck.popleft())
        drawn.add(deck.popleft())

        if pair_exists(hand, hand):
            round += 1
        elif coin >= 1 and pair_exists(hand, drawn):
            coin -= 1
            round += 1
        elif coin >= 2 and pair_exists(drawn, drawn):
            coin -= 2
            round += 1
        else:
            break

    return round


"""
- 분류: 시뮬레이션, 그리디

해설
- 핵심: 현재 라운드까지 뽑은 카드들을 기억해두고, 필요할때 소모해도 됨 (drawn)
    - 이유: 필요할때 가서 받고, 이전 라운드에서 받은 것으로 치면 되기 때문
    - 설명: https://codapul.blogspot.com/2024/01/2024-kakao-winter-internship-n-1.html
- 그리디: 우선순위에 따라 최대한 적은 동전을 소모하며 진행
    - 동전 0개 사용, hand의 2장으로 진행
    - 동전 1개 사용, hand의 1장, drawn의 1장으로 진행
    - 동전 2개 사용, drawn의 2장으로 진행
"""
