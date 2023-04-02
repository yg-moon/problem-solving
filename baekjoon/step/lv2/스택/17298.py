# 오큰수
# 출처: https://ji-gwang.tistory.com/482
N = int(input())
A = list(map(int, input().split()))

stack = []
answer = [-1] * N
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)

"""
- 난이도: 골드4
- 분류: 스택

- 가장 전형적인 유형 ("자신보다 큰 수가 나올때까지" -> 스택)
- 로직을 조금만 개선하면 코드가 훨씬 간단해짐 (스택에 값 대신 인덱스를 저장)
"""
