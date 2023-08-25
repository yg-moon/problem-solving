def solution(phone_book):
    # 모든 숫자를 set에 저장
    num_set = set()
    for num in phone_book:
        num_set.add(num)

    for num in phone_book:
        temp = ""
        # num의 앞자리부터 temp를 하나씩 늘려가면서 확인
        for n in num:
            temp += n
            # temp가 dic에 있는데, temp가 num이 아니라면 접두어인 경우인 것
            if temp in num_set and temp != num:
                return False
    return True
