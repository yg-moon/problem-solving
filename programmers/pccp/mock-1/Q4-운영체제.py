import heapq


def solution(program):
    answer = [0] * 11
    heap = []
    waiting = []
    cur_time = 0

    for a, b, c in program:
        heapq.heappush(heap, (b, a, c))

    while heap or waiting:
        # 다음 작업이 멀리 있을 때
        if heap and not waiting and cur_time < heap[0][0]:
            cur_time = heap[0][0]

        # 대기목록에 추가
        while heap and heap[0][0] <= cur_time:
            b, a, c = heapq.heappop(heap)
            heapq.heappush(waiting, (a, b, c))

        # 목록에서 하나 실행
        a, b, c = heapq.heappop(waiting)
        answer[a] += cur_time - b
        cur_time += c

    answer[0] = cur_time
    return answer


"""
- 분류: 우선순위 큐, 시뮬레이션
- 시간: 4:55-5:30 (30분)

조건
- 점수가 낮을수록 우선순위가 높음
- 우선순위 높은게 먼저 실행, 호출시각 빠른게 먼저 실행

목표
- 모든 프로그램이 종료되는 시각
- 점수가 i인 프로그램들의 대기시간의 합

풀이
- 주의: 현재시각보다 다음 프로그램 실행시간이 멀리 있으면, 현재시각을 당겨와줘야 함

- 현재시각 >= 호출시각인 모든 프로그램을 대기열에 넣음
- 대기열 중에서 우선순위와 호출시각이 가장 먼저인 것을 실행

- 대기시간 계산 = 시작시각 - 호출시각
"""
