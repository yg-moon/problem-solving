from collections import defaultdict
from math import ceil


def solution(fees, records):
    # dic1. {차량번호: [입출차 시간]}
    car_to_records = defaultdict(list)
    # dic2. {차량번호: 총 주차시간}
    car_to_time = defaultdict(int)
    # dic3. {차량번호: 요금}
    car_to_fee = defaultdict(int)

    # dic1 채우기: 차량번호마다 입출차 시간 기록
    for r in records:
        r = r.split()
        car_to_records[r[1]].append(r[0])
    # 입출차 시간 배열의 길이가 홀수라면 "23:59"를 수동으로 추가
    for car in car_to_records:
        if len(car_to_records[car]) % 2 != 0:
            car_to_records[car].append("23:59")

    # dic2 채우기: 주차시간 계산
    for car in car_to_records:
        times = car_to_records[car]
        for i in range(0, len(times), 2):
            in_time = times[i].split(":")
            out_time = times[i + 1].split(":")
            elapsed_time = (int(out_time[0]) - int(in_time[0])) * 60 + (
                int(out_time[1]) - int(in_time[1])
            )
            car_to_time[car] += elapsed_time

    # dic3 채우기: 요금 계산
    for car in car_to_time:
        time = car_to_time[car]
        fee = fees[1]
        if time > fees[0]:
            fee += ceil((time - fees[0]) / fees[2]) * fees[3]
        car_to_fee[car] = fee

    # 차량 번호가 작은 자동차의 요금부터 출력
    answer = sorted(list(car_to_fee.items()))
    answer = [x[1] for x in answer]
    return answer
