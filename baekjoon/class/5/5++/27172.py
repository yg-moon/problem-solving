# 수 나누기 게임
N = int(input())
nums = list(map(int, input().split()))
num_idx_dict = dict()
scores = [0] * N

# dict로 탐색시간 개선
for i in range(N):
    num_idx_dict[nums[i]] = i

# 에라토스테네스의 체 응용
for i in range(N):
    for j in range(nums[i] * 2, 1000001, nums[i]):
        if j in num_idx_dict:
            scores[i] += 1
            scores[num_idx_dict[j]] -= 1

print(*scores)

"""
- 난이도: 골드5
- 분류: 브루트포스, 정수론

- 핵심: 각 카드마다 전체 배열을 돌면서, 자신의 배수를 만나면 경기를 진행 (100만까지 확인)
    - 이렇게 하면 N^2(10만*10만)보다 적은 횟수로 탐색 가능
    - 실제로 계산시 100억 -> 1400만

- 참고: https://uigwonblog.tistory.com/36
"""
