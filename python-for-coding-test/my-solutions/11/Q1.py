n = int(input())
people = list(map(int, input().split()))
people.sort()

group_cnt = 0 # 총 그룹의 수
people_cnt = 0 # 현재 그룹에 포함된 모험가의 수

for scare_val in people: # 공포도를 낮은 것부터 하나씩 확인하며
    people_cnt += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if people_cnt >= scare_val: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group_cnt += 1 # 총 그룹의 수 증가시키기
        people_cnt = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(group_cnt) # 총 그룹의 수 출력
