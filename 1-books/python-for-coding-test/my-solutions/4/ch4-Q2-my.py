loc = input()

al_to_num ={
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}

x = int(loc[1])
y = al_to_num[loc[0]]

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1 ,-2]

cnt = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)
