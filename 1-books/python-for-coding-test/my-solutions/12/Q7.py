# BOJ 18406
N = input()

length = len(N)
left_half = 0
right_half = 0

for i in range(length // 2):
    left_half += int(N[i])
for i in range(length // 2, length):
    right_half += int(N[i])

if left_half == right_half:
    print("LUCKY")
else:
    print("READY")
