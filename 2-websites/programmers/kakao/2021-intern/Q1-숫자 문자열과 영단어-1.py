def solution(s):
    word_to_num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for word in word_to_num:
        while word in s:
            i = s.index(word)
            s = s[:i] + word_to_num[word] + s[i + len(word) :]

    return int(s)


"""
- 분류: 구현
- 소요 시간: 5:00-5:20 (20분)

디버깅
- 런타임 에러
    - 원인: 일부 단어가 바뀌지 않은채로 int() 함수에 들어감
    - 해결: while로 모든 단어를 숫자로 바꿔주었음
"""
