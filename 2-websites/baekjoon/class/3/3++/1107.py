# 리모컨
# 출처: https://velog.io/@jajubal/파이썬백준-1107-리모컨
N = int(input())
M = int(input())

broken = []
if M != 0:
    broken = input().split()

min_move = abs(N - 100)

for num in range(1000001):
    for n in str(num):
        if n in broken:
            break
    # 팁: for-else 문을 사용하면 flag 변수를 생략하고 간결하게 구현 가능.
    else:
        min_move = min(min_move, len(str(num)) + abs(N - num))

print(min_move)

"""
핵심
- 탐색 방식: 0부터 최대 범위까지 모든 숫자를 대입해보며 시도.
- 최대 범위: 간단하게 100만으로 설정.

실행 속도
- 결과: 이 풀이가 7배 정도 빠르다.
- 팁: 재귀는 비용이 크므로 가능하면 반복으로 해결하자.
"""
