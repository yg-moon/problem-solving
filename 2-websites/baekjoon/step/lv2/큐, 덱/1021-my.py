# 회전하는 큐
def solve(target):
    global arr, cur
    cnt = 0
    # 왼쪽 방향 확인
    idx = cur
    left_cnt = 0
    while arr[idx] != target:
        idx = (idx - 1) % len(arr)
        left_cnt += 1
    # 오른쪽 방향 확인
    idx = cur
    right_cnt = 0
    while arr[idx] != target:
        idx = (idx + 1) % len(arr)
        right_cnt += 1
    # 더 가까운 쪽으로 이동해서 삭제
    if left_cnt < right_cnt:
        cur = (cur - left_cnt) % len(arr)
        cnt = left_cnt
    else:
        cur = (cur + right_cnt) % len(arr)
        cnt = right_cnt
    del arr[cur]
    # 배열을 벗어났을 경우 조정
    if cur == len(arr):
        cur = 0  # 주의: cur -= 1 이 아님!
    return cnt


N, M = map(int, input().split())
targets = list(map(int, input().split()))

arr = list(range(1, N + 1))
cur = 0
answer = 0

for t in targets:
    answer += solve(t)
print(answer)

"""
- 난이도: 실버3
- 분류: 덱

- 덱을 사용하지 않고, 좌우로 인덱스를 이동하며 원소를 하나씩 지웠음
"""
