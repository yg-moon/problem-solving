# 출처: 카카오 해설 & 프로그래머스 정답코드
def solution(board, skill):
    R, C = len(board), len(board[0])
    psum = [[0] * (C + 1) for _ in range(R + 1)]

    # 모든 skill에 대해 누적합 배열 초기값 설정
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        set_psum(psum, r1, c1, r2, c2, degree)

    # 위쪽에서 아래쪽으로 누적합 계산
    for j in range(C + 1):
        for i in range(1, R + 1):
            psum[i][j] += psum[i - 1][j]

    # 왼쪽에서 오른쪽으로 누적합 계산
    for i in range(R + 1):
        for j in range(1, C + 1):
            psum[i][j] += psum[i][j - 1]

    # 각 위치의 board와 psum의 합이 0보다 크면 정답
    answer = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] + psum[i][j] > 0:
                answer += 1
    return answer


# 2차원 누적합 배열의 초기값 설정 함수
def set_psum(psum, r1, c1, r2, c2, d):
    psum[r1][c1] += d
    psum[r1][c2 + 1] -= d
    psum[r2 + 1][c1] -= d
    psum[r2 + 1][c2 + 1] += d
