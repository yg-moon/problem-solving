# Kakao 2019
# 출처: 이코테
import heapq


def solution(food_times, k):
    # 예외처리
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐: (음식 시간, 음식 번호)
    Q = []
    for i in range(len(food_times)):
        heapq.heappush(Q, (food_times[i], i + 1))

    prev = 0  # 직전에 다 먹은 음식 시간
    food_len = len(food_times)  # 남은 음식 개수

    # k가 0 이상일 동안, (뺄 음식시간) * (남은 음식 개수)를 k에서 뺀다.
    # while k - ((현재 음식시간 - 이전 음식시간) * 남은 음식 개수) >= 0:
    while k - ((Q[0][0] - prev) * food_len) >= 0:
        now = heapq.heappop(Q)[0]
        k -= (now - prev) * food_len
        food_len -= 1  # 남은 음식 개수 -1
        prev = now  # 이전 음식시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인
    result = sorted(Q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[k % food_len][1]
