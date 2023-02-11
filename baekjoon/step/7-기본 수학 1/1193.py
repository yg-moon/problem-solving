# 분수찾기
X = int(input())

n = 0
diff = 0

for i in range(1, 5000):
    if i * (i + 1) // 2 >= X:
        n = i
        diff = (i * (i + 1) // 2) - X
        break

numer = 1 + diff
denom = n - diff

if n % 2 != 0:
    print(f"{numer}/{denom}")
else:
    print(f"{denom}/{numer}")

"""
- 난이도: 실버5
- 분류: 수학, 구현
"""
