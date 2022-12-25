def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        del_cnt = 0  # 제거한 바위 개수
        base_rock = 0  # 기준점
        for rock in rocks:
            # 기준점과 현재 바위 사이의 거리가 가정한 mid값보다 작으면, 현재 바위를 제거
            if rock - base_rock < mid:
                del_cnt += 1
            # 기준점과 현재 바위 사이의 거리가 mid값보다 크면, 현재 바위가 새로운 기준점
            else:
                base_rock = rock
            # 제거한 바위 개수가 n보다 많으면, for문을 조기에 종료
            if del_cnt > n:
                break

        # 제거한 바위 개수가 n 이하면, 정답을 저장하고 left를 올림
        if del_cnt <= n:
            answer = mid
            left = mid + 1
        # 제거한 바위 개수가 너무 많으면, (가정한 mid값이 큰 것이므로) right를 내림
        else:
            right = mid - 1

    return answer


"""
- 요약: 파라메트릭 서치 응용
- 구현:
    - 이분탐색 대상: 바위 사이 거리의 최솟값
    - 범위조정 기준: 제거한 바위 개수
    - 핵심: 매번 기준점과의 거리를 계산하고, 결과에 따라 현재 바위를 제거하거나 새로운 기준점으로 설정
- 출처: https://cocook.tistory.com/84
"""
