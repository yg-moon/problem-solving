from collections import defaultdict


def solution(enroll, referral, seller, amount):
    parent = defaultdict(str)
    result = defaultdict(int)

    # 부모정보 입력
    for i in range(len(referral)):
        if referral[i] == "-":
            parent[enroll[i]] = "center"
        else:
            parent[enroll[i]] = referral[i]

    # 현재 판매내역을 분배
    def dfs(name, money):
        # 효율성: 남은 금액이 0 이하인 경우 즉시종료하여 가지치기
        if money <= 0 or name == "center":
            return
        tenth = money // 10
        result[name] += money - tenth
        dfs(parent[name], tenth)

    # 모든 판매내역을 분배
    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)

    # 완성된 트리에서 정답 구하기
    answer = []
    for i in range(len(enroll)):
        answer.append(result[enroll[i]])
    return answer


"""
- 난이도: Lv3
- 분류: DFS
- 소요시간: 20분

요약
- 부모에게 10%를 주고, 자신이 나머지를 갖는 과정을 반복
"""
