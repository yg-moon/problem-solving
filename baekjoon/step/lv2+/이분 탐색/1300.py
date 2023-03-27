# K번째 수
# 출처: https://claude-u.tistory.com/449
N = int(input())
K = int(input())
start = 1
end = K  # K번째 수는 K보다 클 수 없으므로

while start <= end:
    mid = (start + end) // 2
    # (설명 참고)
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)
    # 여유가 있으면 정답을 저장하고, 범위를 줄임
    if cnt >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

"""
- 난이도: 골드2
- 분류: 이분탐색

요약
- 이분탐색 대상: 1~K 사이의 수
- 범위조정 기준: 현재 mid보다 작은 (i*j)곱의 개수

설명
- ex. N=10에서, K=20보다 작거나 같은 수는
1*1 ~ 1*10
2*1 ~ 2*10
3*1 ~ 3*6
.
.
.
10*1 ~ 10*2
- 즉, 20(mid)을 행(i)으로 나눈 몫까지다. (단, N을 초과할 수는 없음)
"""
