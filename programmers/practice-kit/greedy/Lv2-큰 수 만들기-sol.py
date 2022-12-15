def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


"""
- 스택을 이용한 그리디 풀이 (여러번 봤던 방법이다!)
    - 매번 스택에 쌓다가, top보다 큰 수가 나오면 while로 전부 pop
- 출처: https://school.programmers.co.kr/questions/29756
"""
