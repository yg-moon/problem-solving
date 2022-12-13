import heapq


def solution(jobs):
    N = len(jobs)
    heapq.heapify(jobs)
    cur_time = 0  # 현재 시각
    total_time = 0  # 요청에서 종료까지 걸린 총 소요시간

    while jobs:
        # 시간이 빌 경우 당겨주기
        if cur_time < jobs[0][0]:
            cur_time = jobs[0][0]

        # 현재 수행할 수 있는 모든 작업을 뽑기
        temp = []
        while jobs and jobs[0][0] <= cur_time:
            temp.append(heapq.heappop(jobs))
        temp.sort(key=lambda x: (x[1], x[0]))

        # 가장 짧은 작업만 처리하고, 나머지는 다시 넣기
        start, length = temp.pop(0)
        cur_time += length
        total_time += cur_time - start
        for job in temp:
            heapq.heappush(jobs, job)

    return total_time // N


"""
- 요약: 매번 현재 수행할 수 있는 모든 작업을 뽑아서, 가장 작은 것만 처리하고 나머지는 다시 넣기
- 구현
    - 현재시각 ≤ 다음 시작시각일 경우, 현재시각을 직접 당겨준다.
    - 현재 수행할 수 있는 모든 작업을 뽑는다. (요청시각 ≤ 현재시각인 작업들)
    - (소요시간, 요청시각) 순서 기준으로 가장 짧은 작업 하나만 처리하고, 나머지는 다시 힙에 넣는다.
- 주의사항
    - 작업이 하나 완료될 때마다, 나머지는 전부 다시 힙에 넣어서 매번 대기 목록을 새로 갱신해야 한다.
    - (이유: 작업이 끝나면 현재시각이 달라져서, 우선순위가 더 높은 새로운 후보가 들어올 수 있으므로)
"""
