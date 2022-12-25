N = 0
visited = []
name_list = []
idx = 0
cnt = 0


def calc_dist(offset):
    global visited, idx
    cur = idx
    dist = 0
    while visited[cur]:
        cur = (cur + offset) % N
        dist += 1
    return dist


def move(index, dir):
    global cnt
    diff = ord(name_list[index]) - ord("A")
    if diff > 13:
        diff = 26 - diff
    cnt += diff
    cnt += dir
    visited[index] = True


def solution(name):
    global N, visited, name_list, idx, cnt
    N = len(name)
    visited = [False] * N
    name_list = list(name)

    # 모든 A는 visited
    for i in range(N):
        if name_list[i] == "A":
            visited[i] = True

    # 첫 글자 처리
    cnt += ord(name_list[0]) - ord("A")
    visited[0] = True

    # 나머지 글자 처리
    while not all(visited):
        left = calc_dist(-1)
        right = calc_dist(1)
        if left < right:
            idx = (idx - left) % N
            move(idx, left)
        else:
            idx = (idx + right) % N
            move(idx, right)

    return cnt


"""
- 그리디 풀이 (테스트케이스 추가로 인해 더 이상 그리디로 해결 불가)
- 요약: 매번 왼쪽과 오른쪽 중에 더 가까운 곳으로 이동
- 구현
    - visited 배열을 만들고, 모든 “A”와 방문한 글자는 방문처리.
    - 매번 왼쪽과 오른쪽을 훑으며 다음 미방문 지점까지의 거리가 더 짧은 곳으로 이동.
    - 주의: 알파벳을 바꿀때도 13번 이상 움직여야 한다면 반대로 움직이는게 더 짧음.
"""
