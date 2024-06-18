import heapq

N = int(input())
K = int(input())
votes = list(map(int, input().split()))

dic = dict()  # {학생 번호: [추천수, 등록순]}
heap = []  # [(추천수, 등록순, 번호), ...]
order = 0

for vote in votes:
    if vote in dic:
        dic[vote][0] += 1
        heapq.heappush(heap, (dic[vote][0], dic[vote][1], vote))
    else:
        # 정렬 풀이: O(NlogN)
        # if len(dic) >= N:
        #     num = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))[0][0]
        #     del dic[num]

        # 힙 풀이: O(logN)
        if len(dic) >= N:
            while heap:
                min_like, cur_order, num = heapq.heappop(heap)
                if dic[num][0] == min_like and dic[num][1] == cur_order:
                    del dic[num]
                    break

        dic[vote] = [1, order]
        heapq.heappush(heap, (1, order, vote))
        order += 1

result = sorted(dic.keys())
print(*result)

"""
N이 커질 경우 효율적인 풀이
- dict + 우선순위 큐
- 배운점: 힙에는 일단 집어넣고, 하나씩 빼면서 실제 정보와 일치하는 내용만 처리해도 됨
"""
