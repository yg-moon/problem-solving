# Z
# 출처: https://dank-code.tistory.com/7
N, r, c = map(int, input().split())
answer = 0


def solve(x, y, n):
    global answer
    if x == r and y == c:
        print(answer)
        exit(0)  # 주의: return 으로는 나머지 함수가 멈추지 않는다.
    if n == 1:
        answer += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        answer += n * n
        return
    half_n = n // 2
    solve(x, y, half_n)
    solve(x, y + half_n, half_n)
    solve(x + half_n, y, half_n)
    solve(x + half_n, y + half_n, half_n)


solve(0, 0, 2**N)

print(answer)

"""
- 난이도: 실버1
- 분류: 분할정복

디버깅
- 메모리 초과
    - 만약 배열을 선언하면 최대 2^30 개의 원소가 필요하다. (4GB)
    - 따라서 배열을 선언하지 않고 풀어야 한다.
- 시간 초과
    - 만약 모든 원소를 탐색하면 최대 2^30 개를 방문해야 한다. 
    - 따라서 모든 원소를 탐색하지 않고 풀어야 한다.
    - 힌트: 재귀함수는 “내가 찾는 범위내에 있을때만 함수를 호출”하여 시간을 줄일 수 있음.

정답
- 기본: 사분면으로 나누어 길이를 절반씩 줄여나간다.
- 핵심
    - 분할된 공간중 (r, c)가 속하는 곳에서만 계속 진행한다.
    - 속하지 않는 공간은 그 크기만큼 num에 더한다.
"""
