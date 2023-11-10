# 가르침
N, K = map(int, input().split())
words = [input() for _ in range(N)]

# 예외처리
if K < 5:
    print(0)
    exit(0)

alps = [False] * 26  # 알파벳별 배움 여부
mid_set = set()
max_cnt = 0

for char in "antic":
    alps[ord(char) - 97] = True

for word in words:
    mid = word[4:-4]  # 앞 anta, 뒤 tica 제외한 단어
    if mid != "":
        for char in mid:
            if char not in "antic":
                mid_set.add(char)

mid_list = list(mid_set)


def dfs(depth, start):
    global max_cnt

    if depth == min(K - 5, len(mid_list)):  # 주의: 종료조건
        cnt = 0
        for word in words:
            can_read = True
            for char in word:
                if not alps[ord(char) - 97]:
                    can_read = False
                    break
            if can_read:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        return

    for i in range(start, len(mid_list)):
        alps[ord(mid_list[i]) - 97] = True
        dfs(depth + 1, i + 1)
        alps[ord(mid_list[i]) - 97] = False


dfs(0, 0)

print(max_cnt)

"""
- 난이도: 골드4
- 분류: 백트래킹

요약
- 가운데서 필요한 단어들의 조합중에서 만족하는게 최대인 개수를 구하기
- 최적화: 백트래킹은 많은 반복이 이루어지므로 최대한 가벼운 연산이 좋음
    - list assignment < list append, pop < set add, remove
    - (백준에서 실행시간 3배 차이)

디버깅
- depth 기준, 즉 어디서 멈출건지에 주의해야 함
- 참고: https://www.acmicpc.net/board/view/27803
"""
