# 수열의 합
N, L = map(int, input().split())

for i in range(L, 101):
    x = N - (i * (i + 1) // 2)
    # 조건1: L로 나누어 떨어질 것
    if x % i == 0:
        x //= i
        # 조건2: 음이 아닌 정수일 것
        if x >= -1:
            for j in range(1, i + 1):
                print(x + j, end=" ")
            print()
            break
else:
    print(-1)

"""
- 난이도: 실버2
- 분류: 수학

- 설명
    - 연속된 L개의 숫자의 합: N = (x+1) + (x+2) + ... + (x+L)
        -> N = Lx + L(L+1)/2
        -> Lx = N - L(L+1)/2
    - x에 대해 식을 정리하고, 조건을 만족하는 길이i (i<=L<=100)을 찾으면 됨
        - 위 식에서 양변에 L로 나누어 떨어지면 x가 정수일 수 있음
        - x가 음이 아닌 정수이어야 하는 조건도 확인하기

- 참고: https://hooongs.tistory.com/334
"""
