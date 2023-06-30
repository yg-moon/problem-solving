# 세 용액
# 출처: https://cieske.tistory.com/64
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_diff = int(3e9)
result = []


def solve():
    global result, min_diff
    for i in range(N - 2):
        ref = arr[i]  # 핵심: 한 점을 고정하기
        l = i + 1
        r = N - 1
        while l < r:
            cur_sum = ref + arr[l] + arr[r]
            # 0에 더 가까운 합을 발견하면 결과를 갱신
            if abs(cur_sum) < abs(min_diff):
                result = [ref, arr[l], arr[r]]
                min_diff = cur_sum
            # 투포인터 이동
            if cur_sum < 0:
                l += 1
            elif cur_sum > 0:
                r -= 1
            else:
                return


solve()
print(*result)

"""
- 난이도: 골드3
- 분류: 투포인터

- 핵심: 한 점을 고정해두고, 나머지 중에서 '두 용액' 문제처럼 찾으면 됨
"""
