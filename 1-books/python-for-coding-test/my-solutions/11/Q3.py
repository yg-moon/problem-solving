# BOJ 1439
# 연속된 0과 1의 묶음 개수를 세서, 적은 쪽이 정답.
s = input()

group_zero = 0
group_one = 0
recent = s[0]

for i in range(1, len(s)):
    # 현재 숫자가 최근 숫자와 다르면 묶음 개수 갱신
    if s[i] != recent:
        if recent == "0":
            group_zero += 1
        else:
            group_one += 1
    # 최근 숫자는 항상 갱신
    recent = s[i]

# 마지막 숫자 처리
if recent == "0":
    group_zero += 1
else:
    group_one += 1

print(min(group_zero, group_one))
