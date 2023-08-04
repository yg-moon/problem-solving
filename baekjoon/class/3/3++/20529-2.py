# 가장 가까운 세 사람의 심리적 거리
# 출처: https://lem0nad3.tistory.com/9
T = int(input())

for _ in range(T):
    N = int(input())
    students = input().split()
    if N >= 33:
        print(0)
    else:
        min_dist = 12
        # combinations 대신 3중 for문
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    cur_dist = 0
                    # 이렇게 하면 같은 조합을 거를 수 있음
                    if i == j or j == k or i == k:
                        continue
                    # 내부로 동작 통합 (사실 함수로 분리하는게 가독성은 더 좋음)
                    for x in range(4):
                        if students[i][x] != students[j][x]:
                            cur_dist += 1
                        if students[j][x] != students[k][x]:
                            cur_dist += 1
                        if students[i][x] != students[k][x]:
                            cur_dist += 1
                    min_dist = min(min_dist, cur_dist)
        print(min_dist)

"""
- 코드가 조금 더 깔끔해서 가져와봄
"""
