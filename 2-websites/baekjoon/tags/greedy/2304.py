# 창고 다각형
arr = []

N = int(input())
for _ in range(N):
    L, H = map(int, input().split())
    arr.append((L, H))

arr.sort()

# 가장 높은 기둥의 위치를 찾기
max_idx = 0
max_height = 0
for i in range(N):
    if arr[i][1] > max_height:
        max_idx = i
        max_height = arr[i][1]

# 가운데 한줄은 미리 계산
answer = max_height

# 왼쪽에서 가운데까지 (다음 기둥과 비교)
height = arr[0][1]
for i in range(max_idx):
    answer += height * (arr[i + 1][0] - arr[i][0])
    if height < arr[i + 1][1]:
        height = arr[i + 1][1]

# 오른쪽에서 가운데까지 (이전 기둥과 비교)
height = arr[-1][1]
for i in range(N - 1, max_idx, -1):
    answer += height * (arr[i][0] - arr[i - 1][0])
    if height < arr[i - 1][1]:
        height = arr[i - 1][1]

print(answer)

"""
- 난이도: 실버2
- 분류: 그리디

핵심: 오목한 부분이 없게
- 제일 큰 기둥의 위치를 찾기
- 왼쪽에서 가운데까지 올라가기만 하기
- 오른쪽에서 가운데까지 올라가기만 하기

참고
- https://velog.io/@holawan/백준-2304창고-다각형-python
"""
