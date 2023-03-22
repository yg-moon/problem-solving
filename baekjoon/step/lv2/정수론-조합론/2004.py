# 조합 0의 개수
# 출처: https://deok2kim.tistory.com/195
n, m = map(int, input().split())


def count(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt


# nCr = n! / ((n-r)! * r!)
two_cnt = count(n, 2) - count(n - m, 2) - count(m, 2)
five_cnt = count(n, 5) - count(n - m, 5) - count(m, 5)
print(min(two_cnt, five_cnt))

"""
- 난이도: 실버2
- 분류: 조합론

핵심
- 끝자리가 0이라는 것은 10의 배수
- 10은 2와 5로 구성되어 있음
- 2와 5의 짝이 맞아야 10이 되므로, 2의 개수와 5의 개수중 더 작은게 10의 개수
"""
