# 가장 긴 바이토닉 부분 수열
# 출처: https://lbdiaryl.tistory.com/167
N = int(input())
arr = list(map(int, input().split()))

LIS = [1] * N  # 가장 긴 증가하는 부분 수열
LDS = [1] * N  # 가장 긴 감소하는 부분 수열
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
            LDS[i] = max(LDS[i], LDS[j] + 1)
LDS.reverse()

# LBS
# 가장 큰 원소를 중복해서 더했으므로 결과에 -1
for i in range(N):
    LBS[i] = LIS[i] + LDS[i] - 1

print(max(LBS))

"""
- 난이도: 골드4
- 분류: dp

- 추가 설명: https://seohyun0120.tistory.com/entry/백준-11054-가장-긴-바이토닉-부분-수열-풀이
"""
