def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    for i in stack:
        answer[i] = len(prices) - 1 - i

    return answer


"""
- 스택을 사용한 O(N) 해법.
    - 스택에 매번 인덱스를 쌓다가, 스택의 top 위치보다 더 낮은 가격이 나오면 while로 pop하며 계산
    - (여태까지는 더 낮은 가격이 안 나왔다는 얘기이므로, 한번에 처리하면 된다는 논리)
"""
