def solution(s: str) -> int:
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
        if word in s:
            s = s.replace(word, word_to_num[word])

    return int(s)


"""
- replace()를 사용한 깔끔한 풀이
"""
