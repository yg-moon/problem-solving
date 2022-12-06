def solution(progresses, speeds):
    n = len(progresses)

    # 배포까지 걸리는 날짜를 계산
    deploys = []
    for i in range(n):
        div, mod = divmod(100 - progresses[i], speeds[i])
        if mod != 0:
            div += 1
        deploys.append(div)

    answer = []
    stack = []
    largest = deploys[0]
    for i in range(n):
        # 기준보다 높은 숫자가 나올때까지 모두 스택에 push
        if deploys[i] <= largest:
            stack.append(deploys[i])
        # 기준보다 높은 숫자가 나오면
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(deploys[i])
            largest = deploys[i]
    # 마지막에 남은것 append
    answer.append(len(stack))
    return answer


"""
- 일단 배포까지 걸리는 날짜 배열을 구하기.
- 날짜 배열을 돌면서
    - 시작점을 기준으로 잡고, 기준보다 높은 숫자가 나올때까지 모두 스택에 push.
    - 기준보다 높은 숫자가 나오면 현재 스택의 크기를 정답에 추가하고, 스택을 비우고, 기준을 갱신.
"""
