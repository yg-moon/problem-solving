# 가장 긴 증가하는 부분 수열2
# 출처: https://jainn.tistory.com/92
# 설명: https://jainn.tistory.com/90
N = int(input())
A = list(map(int, input().split()))

lis = [0]

for a in A:
    # 마지막 값보다 크면 append
    if lis[-1] < a:
        lis.append(a)
    # 아니라면 적절한 위치에 이분탐색으로 삽입
    else:
        left = 0
        right = len(lis)  # 주의: len(LIS)-1 아님
        while left < right:  # 주의: 등호 없음
            mid = (right + left) // 2
            if lis[mid] < a:
                left = mid + 1
            else:
                right = mid  # 주의: mid-1 아님
        lis[right] = a

print(len(lis) - 1)

"""
- 난이도: 골드2
- 분류: 이분탐색, LIS

- 참고: 배열에 최종적으로 들어있는 값들은 실제 LIS를 이루는 요소와 무관함
"""
