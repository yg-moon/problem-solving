array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 매번 끝까지 내려가면서, 바로 옆이 더 크면 스왑.
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
