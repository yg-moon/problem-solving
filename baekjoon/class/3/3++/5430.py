# AC
from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    q = []
    if arr != "[]":
        # 파싱: 맨앞뒤를 제외한 나머지를 , 기준으로 split
        q = deque(map(int, arr[1:-1].split(",")))

    # 핵심: 실제로 뒤집으면 시간초과이므로, 뒤집혔는지 상태만 표시해두고 진행
    rev = False

    for op in p:
        if op == "R":
            rev = not rev
        elif op == "D":
            if not q:
                print("error")
                break
            if rev:
                q.pop()
            else:
                q.popleft()
    else:
        if rev:
            print(str(list(q)[::-1]).replace(" ", ""))  # 주의: 공백 지우기
        else:
            print(str(list(q)).replace(" ", ""))

"""
- 난이도: 골드5
- 분류: 덱, 문자열, 구현
"""
