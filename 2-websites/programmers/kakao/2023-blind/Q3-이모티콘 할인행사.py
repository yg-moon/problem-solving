def solution(users, emoticons):
    rates = [10, 20, 30, 40]
    max_plus_users = 0
    max_profit = 0

    # 각 이모티콘의 할인률 설정
    def dfs(path):
        if len(path) == len(emoticons):
            calc(path)
            return
        for i in range(4):
            path.append(rates[i])
            dfs(path)
            path.pop()

    # 주어진 상황에서 계산
    def calc(path):
        nonlocal max_plus_users, max_profit
        plus_users = 0
        profit = 0

        # 할인가격
        prices = []
        for i in range(len(path)):
            prices.append(int(emoticons[i] * (100 - path[i]) / 100))

        # 모든 사용자에 대해
        for a, b in users:
            cur_sum = 0
            buy_plus = False
            for i in range(len(path)):
                # 일정 비율 이상 할인하면 이모티콘 구매
                if path[i] >= a:
                    cur_sum += prices[i]
                # 합이 일정 금액 이상이면 플러스 가입
                if cur_sum >= b:
                    buy_plus = True
                    break
            if buy_plus:
                plus_users += 1
            else:
                profit += cur_sum

        # 우선순위: 1.가입자수 2.판매액
        if plus_users > max_plus_users:
            max_plus_users = plus_users
            max_profit = profit
        elif plus_users == max_plus_users:
            max_profit = max(max_profit, profit)

    dfs([])

    return [max_plus_users, max_profit]


"""
- 분류: 완전탐색
- 소요 시간: 3:10-3:50 (40분)

요약
- 이모티콘마다 할인율 10, 20, 30, 40 중에 설정
- 해당 상황마다 플러스 가입자수와 매출액을 계산
"""
