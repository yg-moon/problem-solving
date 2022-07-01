# 목표: 가장 많은 그룹을 만드는 것.
# 방법: 제일 작은순으로 나열한 다음, 한명씩 뽑아오기.
import collections

n = int(input())
people = collections.deque(sorted(list(map(int, input().split()))))

group_cnt = 0
group = []
while people:
    group.append(people.popleft())
    if max(group) == len(group):
        group_cnt += 1
        group.clear()

print(group_cnt)
