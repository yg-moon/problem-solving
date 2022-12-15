def solution(n, lost, reserve):
    # 모든 학생이 1로 시작해서, lost에 있으면 -1, reserve에 있으면 +1
    students = [None] + [1] * n  # 1-index
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1

    # 매번 여벌이 있는 학생이 왼쪽, 오른쪽을 확인하며 나눠준다.
    for i in range(1, n + 1):
        if students[i] == 2:
            if i - 1 >= 1 and students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
            elif i + 1 <= n and students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1

    return n - students.count(0)
