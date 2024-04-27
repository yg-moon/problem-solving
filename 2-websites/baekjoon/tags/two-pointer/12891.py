# DNA 비밀번호
from collections import defaultdict

S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())

l = 0
r = P - 1
dic = defaultdict(int)
answer = 0

for char in DNA[:P]:
    dic[char] += 1

while r < S:
    if dic["A"] >= A and dic["C"] >= C and dic["G"] >= G and dic["T"] >= T:
        answer += 1

    dic[DNA[l]] -= 1
    l += 1

    r += 1
    if r < S:
        dic[DNA[r]] += 1

print(answer)

"""
- 난이도: 실버2
- 분류: 투포인터, 슬라이딩 윈도우

디버깅: 시간초과
- 원인: 조건을 잘못 해석함
    - "부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다."
    - 라고 쓰여 있는데 정반대로 해석해서 전부 set에 집어넣느라 시간초과.
"""
