# 보석 도둑
# 출처: https://velog.io/@piopiop/백준-1202-보석-도둑-Python
import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jews = []
for _ in range(N):
    M, V = map(int, input().split())
    jews.append((M, V))
# 보석은 min heap으로 저장
heapq.heapify(jews)

bags = []
for _ in range(K):
    C = int(input())
    bags.append(C)
bags.sort()

answer = 0
tmp_jews = []

# 가장 작은 가방부터 확인
for bag in bags:
    # 1. 현재 가방에 넣을 수 있는 보석들의 가격을 max heap에 저장
    while jews and bag >= jews[0][0]:
        heapq.heappush(tmp_jews, -heapq.heappop(jews)[1])
    # 2. 후보중 최대 가치를 정답에 추가
    # 주의: 나머지 후보는 다음 반복에도 여전히 남아있음
    if tmp_jews:
        answer -= heapq.heappop(tmp_jews)
    # 3. 남은 후보도 없는데, 남은 보석도 없다면 끝났으므로 중단
    elif not jews:
        break

print(answer)

"""
- 난이도: 골드2
- 분류: 그리디, 우선순위 큐

- 핵심: 매번 가장 작은 가방에 가장 비싼 물건을 넣으면 된다는 아이디어
"""
