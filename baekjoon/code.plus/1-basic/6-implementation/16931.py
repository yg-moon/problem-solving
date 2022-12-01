# 겉넓이 구하기
N, M = map(int, input().split())
cube = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


# 상, 하
answer += N * M * 2

# 좌, 우, 앞, 뒤
for _ in range(4):
    cube = rotate(cube)
    for row in cube:
        cur = 0
        for r in row:
            if cur < r:
                answer += r - cur
            cur = r

print(answer)

"""
- 요약: 6방향의 겉넓이를 각각 구해서 더한다.
- 구현
    - 상, 하: N * M
    - 좌, 우, 앞, 뒤
        - 2차원 배열의 각 행마다 진행하면서, 높이가 이전보다 올라갈 경우에만 차이를 겉넓이에 추가.
        - 각 면마다 계산을 위해 배열을 돌리면서 네번 진행하면 끝.
"""
