# 한 줄로 서기
N = int(input())
arr = list(map(int, input().split()))
answer = []

# 핵심: 키의 역순으로 확인하며, 자기보다 왼쪽의 큰 사람수만큼 건너뛰고 삽입
for i in reversed(range(len(arr))):
    answer.insert(arr[i], i + 1)

print(*answer)

"""
- 난이도: 실버2
- 분류: 구현
"""
