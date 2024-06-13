# 한국이 그리울 땐 서버에 접속하지
N = int(input())
pattern = input()
head, tail = pattern.split("*")

for _ in range(N):
    name = input()
    if (
        len(name) >= len(head) + len(tail)  # 주의: 전체길이 확인
        and name[: len(head)] == head
        and name[-len(tail) :] == tail  # 팁: 끝에서부터 n글자를 뽑는 방법
    ):
        print("DA")
    else:
        print("NE")

"""
- 난이도: 실버3
- 분류: 문자열

풀이
- "별표는 항상 가운데 있다" -> 앞단어와 뒷단어를 잘라서, 일치하는지 확인
"""
