# 후보 추천하기
N = int(input())
K = int(input())
votes = list(map(int, input().split()))

pictures = []
like_cnt = []

for vote in votes:
    # 현재 게재된 학생인 경우, 추천수만 증가
    if vote in pictures:
        like_cnt[pictures.index(vote)] += 1
    # 새로운 학생인 경우
    else:
        # 밀어내야 하는 경우
        if len(pictures) >= N:
            idx = like_cnt.index(min(like_cnt))
            del pictures[idx]
            del like_cnt[idx]
        pictures.append(vote)
        like_cnt.append(1)

pictures.sort()
print(*pictures)

"""
- 난이도: 실버1
- 분류: 구현, 시뮬레이션

가장 간단한 풀이
- list에 넣고 순차탐색 (위치만 맞춰주기)
- 들어온 순서대로 삭제: 앞에서부터 지우고, 뒤에다 append

문제점
- N이 커질 경우 비효율적
- (하지만 N이 작아서 복잡한 방법을 쓸 필요도 없음)
"""
