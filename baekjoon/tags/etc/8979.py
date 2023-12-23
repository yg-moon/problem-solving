# 올림픽
N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

# 금, 은, 동 기준으로 정렬
nations.sort(key=lambda x: (-x[1], -x[2], -x[3]))
# 목표의 인덱스 찾기
idx = [nations[i][0] for i in range(N)].index(K)
# 동점자 순위 구하기
for i in range(N):
    if nations[i][1:] == nations[idx][1:]:
        print(i + 1)
        break

"""
- 난이도: 실버5
- 분류: 정렬

핵심
- 번거롭게 계산할 필요없이, 목표의 인덱스를 찾고 동점자의 순위를 구하면 끝
- (동점자가 있는 경우 / 동점자가 없는 경우 / 본인이 1위인 경우가 모두 해결됨)

- 참고: https://develop247.tistory.com/234
"""
