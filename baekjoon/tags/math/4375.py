# 출처: https://merry555.tistory.com/13
while True:
    try:
        n = int(input())
    except:
        break

    cur = 0
    length = 1

    while True:
        cur = cur * 10 + 1
        if cur % n == 0:
            print(length)
            break
        length += 1

"""
- 난이도: 실버3
- 분류: 수학

- 설명
계속 1, 11, 111을 만들어가며
나누어 떨어지면 그것이 배수
"""
