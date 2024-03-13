def solution(coin, cards):
    N = len(cards)
    cards.reverse()
    start_hand = []
    start_coin = coin
    answer = 0

    for _ in range(N // 3):
        start_hand.append(cards.pop())

    # 카드에서 두장을 골라 N+1이 되는 방법 찾기
    def find_target(hand):
        nonlocal N
        result = []
        for i in range(len(hand)):
            for j in range(i + 1, len(hand)):
                if hand[i] + hand[j] == N + 1:
                    result.append([hand[i], hand[j]])
        return result

    # 백트래킹으로 모든 경우를 시도
    def dfs(round, coin, hand, card):
        nonlocal answer

        # 카드 뭉치에 남은 카드가 없다면 게임을 종료
        if not card:
            answer = max(answer, round)
            return

        # 카드를 2장 뽑음
        draw1 = card.pop()
        draw2 = card.pop()

        # 동전 2개를 소모하는 경우
        if coin >= 2:
            cur_coin = coin - 2
            hand.append(draw1)
            hand.append(draw2)
            two_cards = find_target(hand)
            for a, b in two_cards:
                hand.remove(a)
                hand.remove(b)
                dfs(round + 1, cur_coin, hand, card)
                hand.append(a)
                hand.append(b)
            hand.remove(draw1)
            hand.remove(draw2)

        # 동전 1개를 소모하는 경우
        if coin >= 1:
            cur_coin = coin - 1
            hand.append(draw1)  # 1번 카드를 가져가는 경우
            two_cards = find_target(hand)
            for a, b in two_cards:
                hand.remove(a)
                hand.remove(b)
                dfs(round + 1, cur_coin, hand, card)
                hand.append(a)
                hand.append(b)
            hand.remove(draw1)

            hand.append(draw2)  # 2번 카드를 가져가는 경우
            two_cards = find_target(hand)
            for a, b in two_cards:
                hand.remove(a)
                hand.remove(b)
                dfs(round + 1, cur_coin, hand, card)
                hand.append(a)
                hand.append(b)
            hand.remove(draw2)

        # 동전을 소모하지 않은 경우
        two_cards = find_target(hand)
        for a, b in two_cards:
            hand.remove(a)
            hand.remove(b)
            dfs(round + 1, coin, hand, card)
            hand.append(a)
            hand.append(b)

        # 카드 뭉치 복구
        card.append(draw1)
        card.append(draw2)

        # 여기까지 왔으면, 카드 두장을 낼 수 없는 경우이므로 게임을 종료
        answer = max(answer, round)
        return

    dfs(1, start_coin, start_hand, cards)

    return answer


"""
- 백트래킹 풀이: 시간초과

효율성 개선시도
- 데크 대신 거꾸로 뒤집에서 pop을 써볼까?
- 복사를 너무 많이 한듯... 복구하는 방법을 써볼까?
- 두개를 더해서 target이 되는거 더 효율적으로 찾아야 하나?

느낀점
- 시간복잡도를 생각하자. 4^500이면 무슨 수를 써도 불가능이다.
- 처음부터 접근법을 제대로 검증하자.
"""
