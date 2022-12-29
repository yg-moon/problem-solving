# 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())

# 이 로직을 찾는 것이 핵심
div, mod = divmod((V - B), (A - B))
if mod != 0:
    div += 1

print(div)

"""
- 난이도: 브론즈1
- 분류: 수학
"""
