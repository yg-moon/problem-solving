# BOJ 18406
n = input()

length = len(n)
left_half = 0
right_half = 0

for i in range(length // 2):
    left_half += int(n[i])
for i in range(length // 2, length):
    right_half += int(n[i])

if left_half == right_half:
    print("LUCKY")
else:
    print("READY")
