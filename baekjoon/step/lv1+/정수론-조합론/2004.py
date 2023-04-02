# 조합 0의 개수
# 출처: https://deok2kim.tistory.com/195
n, m = map(int, input().split())


def count(num, div):
    cnt = 0
    while num > 0:
        num //= div
        cnt += num
    return cnt


# nCr = n! / ((n-r)! * r!)
two_cnt = count(n, 2) - count(n - m, 2) - count(m, 2)
five_cnt = count(n, 5) - count(n - m, 5) - count(m, 5)
print(min(two_cnt, five_cnt))

"""
- 난이도: 실버2
- 분류: 조합론

로직 해설
- ex. 8!에서 2는 7번 등장한다.
- 구하는 방법:
    - 2의 배수의 개수를 구함 8//2 = 4
    - 제곱수의 개수를 구함 8//(2*2) = 2
    - 세제곱수의 개수를 구함 8//(2*2*2) = 1
    - 4+2+1 = 7
- 설명 출처: https://tmdrl5779.tistory.com/95

핵심
- 끝자리가 0이라는 것은 10의 배수
- 10은 2와 5로 구성되어 있음
- 2와 5의 짝이 맞아야 10이 되므로, 2의 개수와 5의 개수중 더 작은게 10의 개수
"""
