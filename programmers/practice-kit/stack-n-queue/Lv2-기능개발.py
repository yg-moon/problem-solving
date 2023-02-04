def solution(progresses, speeds):
    N = len(progresses)

    # 배포까지 걸리는 날짜를 계산
    deploys = []
    for i in range(N):
        div, mod = divmod(100 - progresses[i], speeds[i])
        if mod != 0:
            div += 1
        deploys.append(div)

    answer = []
    stack = []
    largest = deploys[0]  # 시작점을 기준으로 잡기

    # 날짜 배열을 돌면서
    for i in range(N):
        # 기준보다 높은 숫자가 나올때까지 모두 스택에 push
        if deploys[i] <= largest:
            stack.append(deploys[i])
        # 기준보다 높은 숫자가 나오면
        # - 현재 스택의 크기를 정답에 추가
        # - 스택을 비우고, 현재 숫자로 기준을 갱신하고, 새 기준을 스택에 push
        else:
            answer.append(len(stack))
            stack.clear()
            largest = deploys[i]
            stack.append(deploys[i])

    # 마지막에 남은것 append
    answer.append(len(stack))

    return answer
