# 비밀번호 발음하기
def check(password):
    vowels = list("aeiou")

    # 1. 모음을 반드시 포함
    has_vowel = False
    for char in password:
        if char in vowels:
            has_vowel = True
            break
    if not has_vowel:
        return False

    # 2. 연속으로 모음 3개 혹은 자음 3개 불가
    for i in range(len(password) - 2):
        substr = password[i : i + 3]

        # 자음
        all_vowels = True
        for char in substr:
            if char in vowels:
                all_vowels = False
                break

        # 모음
        all_consonants = True
        for char in substr:
            if char not in vowels:
                all_consonants = False
                break

        if all_vowels or all_consonants:
            return False

    # 3. 같은 글자 두번 허용 금지 (ee, oo 예외)
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and password[i] not in "eo":
            return False

    return True


while True:
    password = input()

    if password == "end":
        break

    if check(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")

"""
- 난이도: 실버5
- 분류: 구현, 문자열

핵심: 복잡한 로직에서 가독성 챙기기
- flag 변수의 이름
- 조건 만족시 바로 리턴해버리기
"""
