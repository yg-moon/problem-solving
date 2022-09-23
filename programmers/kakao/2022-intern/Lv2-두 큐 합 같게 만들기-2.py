# 투포인터 풀이
# 출처: 프로그래머스
def solution(queue1, queue2):
    q = queue1 + queue2
    target_sum = sum(q) // 2

    i, j = 0, len(queue1) - 1
    curr_sum = sum(queue1)
    answer = 0

    while i < len(q) and j < len(q):
        if curr_sum == target_sum:
            return answer
        elif curr_sum < target_sum and j < len(q) - 1:
            j += 1
            curr_sum += q[j]
        else:
            curr_sum -= q[i]
            i += 1
        answer += 1

    return -1
