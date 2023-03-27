# 히스토그램에서 가장 큰 직사각형
# 출처: https://jih3508.tistory.com/75
def solve(l, r):
    global heights
    if l == r:
        return heights[l]
    mid = (r + l) // 2
    # 분할정복: 절반으로 나누었을때 더 큰 부분을 선택
    area = max(solve(l, mid), solve(mid + 1, r))
    # 값 초기화
    lmid = mid
    rmid = mid + 1
    height = min(heights[lmid], heights[rmid])
    area = max(area, height * 2, heights[lmid], heights[rmid])

    # 중앙에서부터 넓혀가며 최대 넓이를 저장
    while l < lmid or rmid < r:  # 양쪽 끝까지 탐색
        # 핵심: 오른쪽으로 확장해야 하는 경우를 확인
        if rmid < r and ((lmid <= l) or (heights[lmid - 1] < heights[rmid + 1])):
            rmid += 1
            height = min(height, heights[rmid])
        # 이외의 경우 왼쪽으로 확장
        else:
            lmid -= 1
            height = min(height, heights[lmid])
        area = max(area, height * (rmid - lmid + 1))
    return area


while True:
    N, *heights = map(int, input().split())
    if N == 0:
        break
    print(solve(0, N - 1))

"""
- 난이도: 플래5
- 분류: 분할정복 (스택, 세그트리도 가능)
"""
