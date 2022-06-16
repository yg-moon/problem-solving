# 같은 풀이지만, 책 구현이 더 깔끔.
n = int(input())

hour = 0
minute = 0
second = 0
cnt = 0

while hour <= n:
    hour += 1
    minute = 0
    while minute <= 59:
        minute += 1
        second = 0
        while second <= 59:
            if "3" in str(hour) + str(minute) + str(second):
                cnt += 1
            second += 1

print(cnt)
