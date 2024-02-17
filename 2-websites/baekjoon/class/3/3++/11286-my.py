# 절댓값 힙
import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    # pop
    if x == 0:
        temp = []
        if heap:
            min_num = heap[0][0]
            while heap and heap[0][0] == min_num:
                temp.append(heapq.heappop(heap))
        # 배열이 비어있는 경우
        if len(temp) == 0:
            print(0)
        # 절댓값이 가장 작은 값이 한개인 경우
        elif len(temp) == 1:
            if temp[0][1] == "+":
                print(temp[0][0])
            else:
                print(-temp[0][0])
        # 절댓값이 가장 작은 값이 여러개인 경우
        else:
            has_minus = False
            for i, t in enumerate(temp):
                if t[1] == "-":
                    print(-t[0])
                    has_minus = True
                    temp.pop(i)
                    break
            if not has_minus:
                item = temp.pop()
                print(item[0])
            for t in temp:
                heapq.heappush(heap, t)
    # push
    else:
        # 양수일 경우
        if x == abs(x):
            heapq.heappush(heap, (x, "+"))
        # 음수일 경우
        else:
            heapq.heappush(heap, (abs(x), "-"))

"""
- 난이도: 실버1
- 분류: 우선순위 큐

- (정답을 보니 쓸데없이 복잡하게 구현했다.)
"""
