def solution(ability):
    student_cnt = len(ability)
    sport_cnt = len(ability[0])
    max_sum = 0

    def dfs(cur_list):
        nonlocal max_sum

        if len(cur_list) == sport_cnt:
            cur_sum = 0
            for i, x in enumerate(cur_list):
                cur_sum += ability[x][i]
            max_sum = max(max_sum, cur_sum)
            return

        for i in range(student_cnt):
            if not visited[i]:
                visited[i] = True
                cur_list.append(i)
                dfs(cur_list)
                cur_list.pop()
                visited[i] = False

    visited = [False] * student_cnt
    dfs([])

    return max_sum


"""
- 분류: 백트래킹, 순열
- 시간: 3:20-3:30 (10분)

- 목표: 각 종목 대표의 해당 종목의 능력치의 합을 최대화
- 방법: 모든 학생들의 순열을 구하기
"""
