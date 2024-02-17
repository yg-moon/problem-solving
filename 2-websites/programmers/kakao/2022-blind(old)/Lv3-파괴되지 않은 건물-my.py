# 정확성 통과, 효율성 실패.
def solution(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        # 공격일 경우
        if type == 1:
            degree *= -1
        # 보드를 돌면서 수정
        for j in range(c1, c2 + 1):
            for i in range(r1, r2 + 1):
                board[i][j] += degree

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer
