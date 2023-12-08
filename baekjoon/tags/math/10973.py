# 이전 순열
N = int(input())
arr = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    # 1. 더 작은 순열을 만들어야 하기에, 큰 수가 앞에 배치된 게 있는지 확인
    if arr[i - 1] > arr[i]:
        for j in range(N - 1, 0, -1):
            # 2. 찾은 수보다 더 작은 수가 앞으로 올 자격이 있음
            if arr[i - 1] > arr[j]:
                arr[i - 1], arr[j] = arr[j], arr[i - 1]
                # 3. 해당 숫자들로 시작하는 제일 마지막 순열 구하기
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr)
                exit(0)
print(-1)

"""
- 난이도: 실버3
- 분류: 수학

- 출처: https://ji-gwang.tistory.com/264
- 설명: https://rrojin.tistory.com/47
"""
