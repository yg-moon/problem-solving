n, m = map(int, input().split())
ducks = list(map(int, input().split()))

ducks.sort()
left = 0
right = n - 1

def binarySearch(left, right):
    while left <= right:
        mid = (left + right) // 2
        d = ducks[mid:]
        
        if sum(d) - ducks[mid]*len(d) > m:
            left = mid + 1
        elif sum(d) - ducks[mid]*len(d) < m:
            right = mid - 1
        else:
            return (True, mid)
    return (False, right)

found, idx = binarySearch(left, right)

# 이진탐색으로 찾지 못했으면, 1씩 증가시키면서 찾기
if not found:
    max_height = ducks[idx]
    # 정답이 떡의 최소 길이보다 작을 때 예외처리
    if idx == -1:
        max_height = 0
    d = ducks[idx+1:]
    while sum(d) - (max_height+1)*len(d) >= m:
        max_height += 1
    print(max_height)
# 이진탐색으로 찾았으면 그대로 출력
else:
    print(ducks[idx])
