# 잃어버린 괄호
# 출처: https://pacific-ocean.tistory.com/228
arr = input().split("-")
nums = []

for a in arr:
    tmp_sum = 0
    splt = a.split("+")
    for s in splt:
        tmp_sum += int(s)
    nums.append(tmp_sum)

answer = nums[0]
for i in range(1, len(nums)):
    answer -= nums[i]

print(answer)

"""
- 난이도: 실버2
- 분류: 그리디

- 핵심: "-" 를 기준으로 split 해서 받는다.
    - ex. 55 - 50 + 40 - 30 + 20 이면
    - ['55', '50 + 40', '30 + 20'] 으로 받는다.
- 리스트의 각 원소를 계산한다.
- 맨 처음 원소만 더해주고 나머지는 빼준다.    
"""
