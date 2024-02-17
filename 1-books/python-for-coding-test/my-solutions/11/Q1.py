N = int(input())
people = list(map(int, input().split()))

people.sort()

group_cnt = 0
people_cnt = 0

for scare_val in people:
    people_cnt += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if people_cnt >= scare_val:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group_cnt += 1
        people_cnt = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(group_cnt)
