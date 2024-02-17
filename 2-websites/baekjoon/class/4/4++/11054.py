# 가장 긴 바이토닉 부분 수열
# 출처: https://lbdiaryl.tistory.com/167
N = int(input())
arr = list(map(int, input().split()))

LIS = [1] * N  # 가장 긴 증가하는 부분 수열
LDS2 = [1] * N  # 현재 수'부터' 가능한 가장 긴 감소하는 부분 수열 (원래 LDS는 현재 수'까지')
LBS = [0] * N  # 가장 긴 바이토닉 부분 수열

# LIS
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

# LDS
# 주어진 수열을 뒤집고, LIS를 구하고, dp 배열을 다시 뒤집기
arr.reverse()
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            LDS2[i] = max(LDS2[i], LDS2[j] + 1)
LDS2.reverse()

# LBS
# 가장 큰 원소를 중복해서 더했으므로 결과에 -1
for i in range(N):
    LBS[i] = LIS[i] + LDS2[i] - 1

print(max(LBS))

"""
- 난이도: 골드4
- 분류: dp

- 추가 설명: https://seohyun0120.tistory.com/entry/백준-11054-가장-긴-바이토닉-부분-수열-풀이
"""
