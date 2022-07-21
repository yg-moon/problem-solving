import collections
import math


def solution(fees, records):
    # dict1: 차 번호 - [시간 정보]
    car_to_records = collections.defaultdict(list)
    # dict2: 차 번호 - 누적 주차 시간
    car_to_total_time = collections.defaultdict(int)
    # dict3: 차 번호 - 주차 요금
    car_to_fee = collections.defaultdict(int)

    # dict1 채우기.
    for record in records:
        r = record.split()
        car_to_records[r[1]].append(r[0])

    # 시간 정보 배열의 길이 홀수면 "23:59"를 직접 추가하기.
    for car in car_to_records:
        if len(car_to_records[car]) % 2 != 0:
            car_to_records[car].append("23:59")

    # dict2 채우기.
    for car in car_to_records:
        time = 0
        while car_to_records[car]:
            out_time = car_to_records[car].pop()
            in_time = car_to_records[car].pop()
            o = out_time.split(":")
            i = in_time.split(":")
            hour = (int(o[0]) - int(i[0])) * 60
            minute = int(o[1]) - int(i[1])
            time += hour
            time += minute
        car_to_total_time[car] = time

    # dict3 채우기.
    for car in car_to_total_time:
        fee = fees[1]
        if car_to_total_time[car] > fees[0]:
            fee += math.ceil((car_to_total_time[car] - fees[0]) / fees[2]) * fees[3]
        car_to_fee[car] = fee

    # 정렬해서 결과 리턴하기.
    answer = sorted(list(car_to_fee.items()))
    answer = [x[1] for x in answer]
    return answer
