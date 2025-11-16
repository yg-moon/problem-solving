# 떡 먹는 호랑이
D, K = map(int, input().split())


def sol():
    # 각 계수에 대한 피보나치 수열
    dp_a = [0] * 31
    dp_b = [0] * 31

    # 초기화
    dp_a[1] = 1
    dp_a[2] = 0
    dp_b[1] = 0
    dp_b[2] = 1

    # 점화식
    for i in range(3, D + 1):
        dp_a[i] = dp_a[i - 1] + dp_a[i - 2]
        dp_b[i] = dp_b[i - 1] + dp_b[i - 2]

    # 일차방정식 해결: 대입법
    for A in range(1, K + 1):
        B, mod = divmod(K - dp_a[D] * A, dp_b[D])
        if mod == 0:
            print(A)
            print(B)
            return


sol()

"""
- 난이도: 실버1
- 분류: dp, 브루트포스

풀이
- a와 b의 계수에 대한 피보나치 수열이 각각 생김을 확인
- 'dp_a[D]*a + dp_b[D]*b = K' 일차방정식을 해결
"""
