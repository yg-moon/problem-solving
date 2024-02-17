def solve(n, p):
    if n == 1:
        return "Rr"

    parent = solve(n - 1, (p - 1) // 4 + 1)

    if parent == "RR" or parent == "rr":
        return parent
    else:
        if p % 4 == 0:
            return "rr"
        elif p % 4 == 1:
            return "RR"
        else:
            return "Rr"


def solution(queries):
    answer = []

    for n, p in queries:
        answer.append(solve(n, p))

    return answer


"""
- 분류: 재귀
- 시간: 3:40-4:30 (50분)

내 풀이
- n세대의 p번째 = n-1세대의 {p//4 + (mod>1)}번의 mod번째 자손
- 맨 윗세대까지 올라가서, 다시 내려오면서 형질을 추적

더 깔끔한 풀이
- n세대의 p번째 = n-1세대의 {(p-1)//4 + 1}번의 mod번째 자손
- 맨 윗세대까지 올라가서, 다시 내려오면서 형질을 추적

- 아이디어는 비슷한데, 추적하는 과정을 재귀적으로 처리
- 매번 부모를 구하고, 그에 따른 결과를 리턴
    - 부모가 RR or rr이면 그대로 리턴
    - 부모가 Rr이면 (p % 4)의 결과를 리턴

- 출처: https://dmaolon00.tistory.com/entry/PrgrammersPython-유전-법칙
"""
