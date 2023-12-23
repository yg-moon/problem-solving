# 팰린드롬 만들기
from collections import defaultdict

s = input()

# 각 문자가 몇번 등장했는지 기록
dic = defaultdict(int)
for char in s:
    dic[char] += 1

# 문자열을 오름차순 정렬하고 홀수번 등장한 문자를 기록
# 이 때 홀수번 등장한 문자가 2번 이상이면 I'm Sorry를 출력하고 종료
keys = sorted(dic.keys())
odd_char = ""
for key in keys:
    if dic[key] % 2 == 1:
        if odd_char == "":
            odd_char = key
        else:
            print("I'm Sorry Hansoo")
            exit(0)

# 사전순으로 문자열들을 절반번 반복하고
# 홀수번 나오는 문자열이 있다면 이어붙이고
# 앞쪽의 문자열을 뒤집어서 이어붙여서 팰린드롬을 만들기
answer = ""
temp = ""
for key in keys:
    cnt = dic[key] // 2
    temp += key * cnt
    dic[key] = int(dic[key] / 2)  # 홀수번 등장하는 경우가 있기 때문에 int 함수로 내림
answer += temp

if odd_char != "":
    answer += odd_char

answer += temp[::-1]

print(answer)

"""
- 난이도: 실버3
- 분류: 문자열, 그리디

- 출처: https://v3.leedo.me/devs/62
"""
