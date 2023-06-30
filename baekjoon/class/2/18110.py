# solved.ac
import sys

input = sys.stdin.readline


def round_off(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(input())

if n == 0:
    print(0)
else:
    lst = [int(input()) for _ in range(n)]
    lst.sort()
    cut = round_off(n * 0.15)
    print(round_off(sum(lst[cut : n - cut]) / (n - cut * 2)))

"""
- 난이도: 실버4
- 분류: 수학 (반올림)

- 배운점: 파이썬의 round()는 오사오입이므로, 사사오입이 필요할 경우 직접 구현해야 한다.

참고
1. 사사오입(round-off)
- 4까지는 버림, 5부터는 올림 (ex. 1.5 -> 2, 2.5 -> 3)
2. 오사오입(round-to-nearest-even)
- 4까지는 버림, 6부터는 올림
- 5는 앞자리에 따라 결과가 짝수가 되도록 처리 (ex. 1.5 -> 2, 2.5 -> 2)
"""
