def solution(board, skill):
    R, C = len(board), len(board[0])
    psum = [[0] * (C + 1) for _ in range(R + 1)]

    # 모든 skill에 대해 누적합 배열 초기값 설정
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        psum[r1][c1] += degree
        psum[r1][c2 + 1] -= degree
        psum[r2 + 1][c1] -= degree
        psum[r2 + 1][c2 + 1] += degree

    # 위쪽 -> 아래쪽 누적합 계산
    for i in range(1, R + 1):
        for j in range(C + 1):
            psum[i][j] += psum[i - 1][j]

    # 왼쪽 -> 오른쪽 누적합 계산
    for i in range(R + 1):
        for j in range(1, C + 1):
            psum[i][j] += psum[i][j - 1]

    # 각 위치의 board와 psum의 합이 0보다 크면 정답+1
    answer = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] + psum[i][j] > 0:
                answer += 1
    return answer


"""
- 분류: 누적합 (2차원)
- 출처: 카카오 해설 & 프로그래머스 정답코드

핵심: "배열의 a번째 원소부터 b번째 원소까지 c만큼의 변화를 주겠다고 하면,
     새로운 배열의 a번째 원소에 c를 더하고 b+1번째 원소에 c를 빼면 됩니다."

1. 초기값 설정
n 0 0 -n
0 0 0 0
0 0 0 0
-n 0 0 n

2. 위에서 아래로, 왼쪽에서 오른쪽으로 누적합 하면
n n n 0
n n n 0
n n n 0
0 0 0 0

3. 원본 배열과 더하면 (0,0)~(2,2) 까지 n을 적용하게 됨
"""
