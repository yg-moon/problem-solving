# 유레카 이론
tri_nums = [n * (n + 1) // 2 for n in range(1, 46)]
eureka = [0] * 1001

# 핵심: 3중 for문으로, 모든 입력에 대한 결과를 미리 계산해두기
for i in tri_nums:
    for j in tri_nums:
        for k in tri_nums:
            if i + j + k <= 1000:
                eureka[i + j + k] = 1

T = int(input())
for _ in range(T):
    print(eureka[int(input())])

"""
- 난이도: 브론즈1
- 분류: 수학, 브루트포스
"""
