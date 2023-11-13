def solution(queue1, queue2):
    q = queue1 + queue2
    target_sum = sum(q) // 2
    cur_sum = sum(queue1)
    answer = 0

    # q1의 양끝에 포인터를 두고 시작
    i = 0
    j = len(queue1) - 1

    while i < len(q) and j < len(q):
        if cur_sum == target_sum:
            return answer
        elif cur_sum < target_sum and j < len(q) - 1:  # 주의: 인덱스 예외처리 필요
            j += 1
            cur_sum += q[j]
        else:
            cur_sum -= q[i]
            i += 1
        answer += 1

    return -1


"""
- 투포인터 풀이
- 출처: 프로그래머스
"""
