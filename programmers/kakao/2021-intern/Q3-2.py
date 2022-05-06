def solution(n, k, cmd):
    # 테이블 채우기
    table = []
    for i in range(n):
        table.append(i)

    # 현재 위치 지정
    curr = k

    # 삭제된 요소들
    removed = []

    # cmd 처리
    for command in cmd:
        if command[0] == "U":
            cnt = 0
            while cnt != int(command[2:]):
                curr -= 1
                if table[curr] is not None:
                    cnt += 1
        elif command[0] == "D":
            cnt = 0
            while cnt != int(command[2:]):
                curr += 1
                if table[curr] is not None:
                    cnt += 1
        elif command[0] == "C":
            table[curr] = None
            removed.append(curr)
            isEnd = False
            saved_curr = curr
            # 그냥 맨 끝인 경우
            if curr + 1 >= n:
                isEnd = True
            # 밑에 바로 있는 경우
            elif curr + 1 < n and table[curr + 1] is not None:
                curr += 1
            # 밑에 건너뛰어 있는 경우
            else:
                while curr + 1 < n and table[curr] is None:
                    curr += 1
                # 사실은 맨 끝이었던 경우
                if table[curr] is None:
                    isEnd = True
            # 위로 올라오기
            if isEnd:
                curr = saved_curr
                # 바로 위가 있는 경우
                if table[curr - 1] is not None:
                    curr -= 1
                # 위로 있을 때 까지 올라가기
                else:
                    curr -= 1
                    while table[curr] is None:
                        curr -= 1
        elif command[0] == "Z":
            restored = removed.pop()
            table[restored] = restored

    # 정답 만들기
    answer = ["O"] * n
    for i in range(n):
        if table[i] is None:
            answer[i] = "X"
    return "".join(answer)
