# 냅색문제
# 출처: https://baebalja.tistory.com/254
# 추가설명: https://myunji.tistory.com/364
from bisect import bisect_right

N, C = map(int, input().split())
things = list(map(int, input().split()))

# 물건 개수를 기준으로 절반으로 나누고, 각각 dfs를 돌린 결과를 저장
part1 = []
part2 = []


def dfs(start, end, part, cur_sum, th):
    # 끝까지 도달했으면 해당 조합의 무게 합을 저장
    if start > end:
        part.append(cur_sum)
        return
    # 물건을 담는지, 안 담는지 여부로 나누어 재귀
    else:
        dfs(start + 1, end, part, cur_sum, th)
        dfs(start + 1, end, part, cur_sum + th[start], th)


dfs(0, N // 2 - 1, part1, 0, things)
dfs(N // 2, N - 1, part2, 0, things)

part2.sort()

answer = 0
for i in range(len(part1)):
    # 더 담을 수 있는 최대무게 = 가방의 무게 - part1[i]
    x = C - part1[i]
    # part2에서 이분탐색으로 찾은 위치: 더 담을 수 있는 최대무게 이하인 값들의 개수
    answer += bisect_right(part2, x)

print(answer)

"""
- 난이도: 골드1
- 분류: 투포인터

- Meet in the middle (MITM) 알고리즘
"""
