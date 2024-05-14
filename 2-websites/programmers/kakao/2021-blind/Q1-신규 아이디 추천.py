def solution(new_id):
    result = []

    # 1
    result = list(new_id.lower())

    # 2
    temp = []
    for ch in result:
        if ch.isalnum() or ch in "-_.":
            temp.append(ch)
    result = temp

    # 3
    temp = []
    for i in range(len(result)):
        if i < len(result) - 1 and result[i] == "." and result[i + 1] == ".":
            continue
        temp.append(result[i])
    result = temp

    # 4
    if result[0] == ".":
        if result[-1] == ".":
            result = result[1:-1]
        else:
            result = result[1:]
    elif result[-1] == ".":
        result = result[:-1]

    # 5
    if not result:
        result.append("a")

    # 6
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == ".":
            result.pop()

    # 7
    if len(result) <= 2:
        ch = result[-1]
        for _ in range(3 - len(result)):
            result.append(ch)

    return "".join(result)


"""
- 분류: 문자열, 구현

요약
- 시키는 대로 구현
- 유효한 문자만 추리는 방식으로 하면 효율적
"""
