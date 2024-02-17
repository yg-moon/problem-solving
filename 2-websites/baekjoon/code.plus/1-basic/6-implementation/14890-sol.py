# 경사로
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def check_line(line):
    for i in range(1, N):
        # 차이가 2 이상일 경우 즉시 종료
        if abs(line[i] - line[i - 1]) > 1:
            return False
        # 현재 < 이전일 경우: 오른쪽을 쭉 확인
        if line[i] < line[i - 1]:
            for j in range(L):
                # 범위 넘어감 or 높이가 다름 or 이미 설치했을 경우, 종료
                if i + j >= N or line[i] != line[i + j] or slope[i + j]:
                    return False
                # 경사로 설치
                slope[i + j] = True
        # 현재 > 이전일 경우: 왼쪽을 쭉 확인
        elif line[i] > line[i - 1]:
            for j in range(L):
                # 범위 넘어감 or 높이가 다름 or 이미 설치했을 경우, 종료
                # 주의: 모든 작업을 현재 위치가 아니라 한칸 왼쪽(-1)에서 해야함
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                # 경사로 설치
                slope[i - j - 1] = True
    return True


# 각 행에 대해 확인
for i in range(N):
    slope = [False] * N
    if check_line([board[i][j] for j in range(N)]):
        answer += 1

# 각 열에 대해 확인
for j in range(N):
    slope = [False] * N
    if check_line([board[i][j] for i in range(N)]):
        answer += 1

print(answer)

"""
출처
- 코드: https://velog.io/@ms269/백준-14890-경사로-파이썬-Python
- 주석: https://ryu-e.tistory.com/108
"""
