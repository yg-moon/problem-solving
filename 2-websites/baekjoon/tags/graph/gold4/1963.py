# 소수 경로
from collections import deque


def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solve(num1, num2):
    q = deque()
    q.append(list(num1))
    dist = [-1] * 10000
    dist[int(num1)] = 0

    while q:
        cur_list = q.popleft()
        cur_num = int("".join(cur_list))

        if cur_num == int(num2):
            return dist[cur_num]

        for i in range(4):
            for j in range(10):
                temp_list = cur_list[:]
                temp_list[i] = str(j)
                temp_num = int("".join(temp_list))
                if temp_num >= 1000 and is_prime(temp_num) and dist[temp_num] == -1:
                    q.append(temp_list[:])
                    dist[temp_num] = dist[cur_num] + 1

    return -1


T = int(input())

for _ in range(T):
    num1, num2 = input().split()
    result = solve(num1, num2)
    if result != -1:
        print(result)
    else:
        print("Impossible")

"""
- 난이도: 골드4
- 분류: BFS
- 소요 시간: 30분

핵심
- 앞에서부터 모든 자리수를 0~9로 바꿔보고, 소수인 경우 큐에 삽입
- 문자 리스트로 관리했다가 합치면서 정수로 바꾸는게 구현적인 디테일
"""
