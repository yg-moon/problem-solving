def solution(phone_book):
    # 모든 숫자를 딕셔너리에 저장
    dic = {}
    for num in phone_book:
        dic[num] = 1

    for num in phone_book:
        temp = ""
        # num의 앞자리부터 temp를 하나씩 늘려가면서 확인
        for n in num:
            temp += n
            # temp가 dic에 있는데, temp가 num이 아니라면 접두어인 경우인 것
            if temp in dic and temp != num:
                return False
    return True
