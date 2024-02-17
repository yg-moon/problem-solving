# BOJ 1759
# 출처: 이코테
# 훨씬 풀이가 간결함.
from itertools import combinations

vowels = ("a", "e", "i", "o", "u")
L, C = map(int, input().split(" "))

array = input().split(" ")
array.sort()

# 길이가 L인 모든 암호 조합을 확인
for password in combinations(array, L):
    cnt = 0
    for p in password:
        if p in vowels:
            cnt += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if cnt >= 1 and cnt <= L - 2:
        print("".join(password))
