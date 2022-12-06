def solution(prices):
    answer = []
    for i in range(len(prices)):
        days = 0
        for j in range(i + 1, len(prices)):
            days += 1
            if prices[i] > prices[j]:
                break
        answer.append(days)
    return answer


"""
- 스택을 쓰지 않고 2중 for문 사용.
- 나이브한 O(N^2) 해법.
"""
