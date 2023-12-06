# 팰린드롬 만들기
from collections import defaultdict

name = input()

# 각 문자에 대한 개수를 셈
dic = defaultdict(int)
for char in name:
    dic[char] += 1

result = [""] * len(name)
keys = sorted(dic.keys())  # 사전순으로 찾기 위해 정렬
l = 0
r = len(name) - 1

# 투포인터로 좌우에서 좁혀가면서
while l <= r:
    # 가운데라면 1개 이상 남은 문자를 삽입
    if l == r:
        for key in keys:
            if dic[key] >= 1:
                result[l] = key
                break
    # 좌우에 2개 이상 남은 문자를 삽입
    else:
        for key in keys:
            if dic[key] >= 2:
                result[l] = key
                result[r] = key
                dic[key] -= 2
                break
    l += 1
    r -= 1

# 주의: 팰린드롬이 안되는 조건을 정확히 설정 (이것 때문에 삽질함)
if "" in result:
    print("I'm Sorry Hansoo")
else:
    print("".join(result))

"""
- 난이도: 실버3
- 분류: 문자열, 그리디, 투포인터
"""
