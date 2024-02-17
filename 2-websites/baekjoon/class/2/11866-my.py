# 요세푸스 문제 0
N, K = map(int, input().split())

if N == 1:
    print("<1>")
else:
    people = list(range(1, N + 1))
    result = []
    idx = 0

    while len(result) != N:
        idx = (idx + (K - 1)) % len(people)
        val = people[idx]
        result.append(val)
        people.remove(val)

    for i, r in enumerate(result):
        if i == 0:
            print(f"<{r}, ", end="")
        elif i == len(result) - 1:
            print(f"{r}>")
        else:
            print(f"{r}, ", end="")

"""
- 난이도: 실버5
- 분류: 구현, 큐
"""
