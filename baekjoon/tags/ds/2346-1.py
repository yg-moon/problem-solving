# 풍선 터뜨리기
from collections import deque

N = int(input())
q = deque(enumerate(map(int, input().split())))
result = []

while q:
    # 핵심: (idx, val)로 묶어서 데크 안에서 돌리기
    idx, val = q.popleft()
    result.append(idx + 1)

    # 양수면 오른쪽으로 이동 = 데크를 왼쪽으로 회전 = rotate(음수)
    if val > 0:
        # 주의: 삭제하면 이미 한칸 오른쪽으로 이동하므로 -1
        q.rotate(-(val - 1))
    # 음수면 왼쪽으로 이동 = 데크를 오른쪽으로 회전 = rotate(양수)
    else:
        q.rotate(-val)

print(*result)

"""
- 난이도: 실버3
- 분류: 자료구조(덱)
"""
