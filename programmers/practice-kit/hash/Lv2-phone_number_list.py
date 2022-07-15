# 출처: https://programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3
def solution(phone_book):
    # 모든 숫자를 딕셔너리에 저장
    dic = {}
    for num in phone_book:
        dic[num] = 1

    # num의 앞자리부터 temp를 하나씩 늘려가면서 확인
    # temp가 dic에 있는데, temp가 num이 아니라면 접두어인 경우인 것
    for num in phone_book:
        temp = ""
        for n in num:
            temp += n
            if temp in dic and temp != num:
                return False

    return True
