cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]


def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            # 첫 행과 첫 열은 모두 0 으로 채우기
            if i == 0 or c == 0:
                pack[i].append(0)
            
            # 이전 짐의 무게 <= 현재 배낭 용량
            elif cargo[i - 1][1] <= c:
                # 현재 위치에 두 후보중 더 큰 값을 기록한다:
                pack[i].append(
                    max(
                        # 후보1. 이전 짐의 가치 + 셀 값: [이전 짐 개수][현재 배낭 용량 - 이전 짐의 무게] 에서의 최대 가치
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        # 후보2. 셀 값: [이전 짐 개수][현재 배낭 용량] 에서의 최대 가치
                        pack[i - 1][c]
                    ))
            # 이전 짐의 무게 > 현재 배낭 용량
            else:
                # 현재 셀값도, 이전 셀값 [이전 짐 개수][현재 배낭 용량] 으로 채우기.
                pack[i].append(pack[i - 1][c])
    
    # 셀 값: [최대 짐 개수][최대 배낭 용량] 에서의 최대 가치
    return pack[-1][-1]


r = zero_one_knapsack(cargo)
print(r)
