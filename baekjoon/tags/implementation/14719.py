# 빗물
H, W = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in range(1, W - 1):
    l_max = max(arr[:i])
    r_max = max(arr[i + 1 :])
    lower_max = min(l_max, r_max)
    if arr[i] < lower_max:
        answer += lower_max - arr[i]

print(answer)

"""
- 난이도: 골드5
- 분류: 시뮬레이션

핵심
- 전제: 물이 고이려면 왼쪽과 오른쪽에 자신보다 높은 블럭이 있어야 함
- 결론: 따라서 처음과 끝을 제외한 각 열마다 물이 얼만큼 고이는지 계산하기

출처
- https://velog.io/@rhdmstj17/백준-14719번-빗물-python-시뮬레이션-골드-5
"""
