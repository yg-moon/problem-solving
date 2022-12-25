def solution(n, times):
    times.sort()
    answer = 0
    left, right = 1, max(times) * n
    # right: 가장 비효율적으로 심사했을 때 걸리는 시간
    # 즉, 가장 심사시간이 긴 심사관에게 n명 모두 심사받는 경우

    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            # people: 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나감
            if people >= n:
                break
        # 심사를 받은 사람의 수가 n이상일 경우, 현재 답을 저장하고 right를 내림
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사를 받은 사람의 수가 n미만일 경우, left를 올림
        else:
            left = mid + 1

    return answer


"""
- 요약: 파라메트릭 서치 기본
- 구현:
    - 이분탐색의 대상: ‘모든 사람이 심사를 받는데 걸린 시간’
    - 범위조정의 기준: ‘심사를 받은 사람의 수’
- - 출처: https://sohee-dev.tistory.com/123
"""
