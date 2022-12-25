from itertools import permutations

# 알파벳이 주어졌을 때 상하로 움직이는 횟수를 구하는 함수
def countChanges(char):
    return min(ord("Z") - ord(char) + 1, ord(char) - ord("A"))


# 왼쪽, 오른쪽 중 최단거리를 구하는 함수
def findShortestPath(name, cur, next):
    left, right = min(cur, next), max(cur, next)
    leftDist = left + len(name) - right
    rightDist = right - left
    return min(leftDist, rightDist)


def solution(name):
    answer = int(1e9)

    # "A" 가 아니라서 가야하는 위치(시작 위치 제외)
    dests = [i for i in range(len(name)) if name[i] != "A" and i != 0]

    # 알파벳을 바꾸느라 필요한 조이스틱 이동
    changeCount = 0
    for c in name:
        changeCount += countChanges(c)

    # 움직일 수 있는 모든 경우의 수
    perms = permutations(dests, len(dests))
    for perm in perms:
        cur = 0
        moveCount = 0
        for next in perm:
            dist = findShortestPath(name, cur, next)
            moveCount += dist
            cur = next
        answer = min(answer, moveCount + changeCount)

    return answer


"""
- 완전탐색 풀이
- 출처: https://kjhoon0330.tistory.com/entry/프로그래머스-조이스틱-Python)
"""
