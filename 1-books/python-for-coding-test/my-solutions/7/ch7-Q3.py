N, M = list(map(int, input().split(" ")))
arr = list(map(int, input().split()))

start = 0
end = max(arr)

# 이진탐색 (반복구현)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 덜 자르기 (왼쪽 부분 탐색)
    if total < M:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 더 자르기 (오른쪽 부분 탐색)
    else:
        # 최대한 많이 잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid
        start = mid + 1

print(result)
