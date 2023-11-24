def solution(today, terms, privacies):
    type_to_life = dict()
    answer = []

    # 약관별 유효기간
    for term in terms:
        type, life = term.split()
        type_to_life[type] = int(life)

    # 개인정보마다 계산
    for i in range(len(privacies)):
        date, type = privacies[i].split()
        yy, mm, dd = map(int, date.split("."))

        # 핵심: 파기날짜 계산
        carry, mm = divmod(mm + type_to_life[type], 12)
        if mm == 0:
            mm = 12
            carry -= 1
        yy += carry

        # 파기날짜 형식 조정
        lst = [str(yy) + "."]
        if mm < 10:
            lst.append("0" + str(mm) + ".")
        else:
            lst.append(str(mm) + ".")
        if dd < 10:
            lst.append("0" + str(dd))
        else:
            lst.append(str(dd))
        expiry = "".join(lst)

        # 현재날짜와 비교하여 파기여부 결정
        if today >= expiry:
            answer.append(i + 1)

    return answer


"""
- 분류: 구현
- 소요 시간: 1:05-1:50 (45분)

생각
- 날짜 계산은 어떻게? -> month만큼만 더하기 (day는 건들지 말기)
- 날짜 비교는 어떻게? -> 원래 형식으로 통일해서 문자열 비교

주의
- 100개월까지 더해질 수 있으므로, 올림 고려하기
- 5월19일에서 1달 보관가능시 6월19일에는 파기해야 하므로, 등호 주의하기
"""
