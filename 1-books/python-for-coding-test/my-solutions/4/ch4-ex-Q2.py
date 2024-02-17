N = int(input())
cnt = 0

for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            if "3" in str(hour) + str(minute) + str(second):
                cnt += 1

print(cnt)
