# 분수찾기
X = int(input())
n = 0  # X가 몇층에 있는지
diff = 0  # 해당 층에서 몇칸 이동해야 하는지

for i in range(1, 5000):
    # n: 1부터 i까지 더했을때 X보다 크거나 같아지는 i의 최솟값
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
- 분류: 수학
"""
