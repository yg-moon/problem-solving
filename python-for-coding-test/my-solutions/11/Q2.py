# 목표: 가장 큰 수 만들기
# 방법: 가능하면 무조건 곱하고, 0이나 1이면 더하기.
num_str = input()

result = int(num_str[0])

for i in range(1, len(num_str)):
    n = int(num_str[i])
    if result <= 1 or n <= 1:
        result += n
    else:
        result *= n

print(result)
