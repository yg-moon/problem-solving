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
        start_time, duration = temp.pop(0)
        cur_time += duration
        total_time += cur_time - start_time
        for job in temp:
            heapq.heappush(jobs, job)

    return total_time // N


"""
- 요약: 매번 현재 수행할 수 있는 모든 작업을 뽑아서, 가장 작은 것만 처리하고 나머지는 다시 넣기
"""
