def solution(input_string):
    seen = set()
    lonely = set()
    last = input_string[0]

    for char in input_string:
        if char in seen and last != char:
            lonely.add(char)
        seen.add(char)
        last = char

    answer = "".join(sorted(lonely))
    return answer if answer else "N"


"""
- 전체 문제 확인: 3:05-3:10 (5분)

- 분류: 문자열, 구현
- 시간: 3:10-3:15 (5분)

- 목표: 외톨이 알파벳을 찾아서, 오름차순으로 정렬
- 방법:
    - 하나씩 돌면서 seen에 넣고, last를 추적
    - seen에 있는데 last와 다르다면 외톨이
"""
