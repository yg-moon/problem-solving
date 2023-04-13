# 30
# 출처: https://yoonsang-it.tistory.com/36
N = input()

if "0" not in N:
    print(-1)
else:
    sum_N = 0
    for i in range(len(N)):
        sum_N += int(N[i])

    if sum_N % 3 != 0:
        print(-1)
    else:
        answer = "".join(sorted(N, reverse=True))
        print(answer)

"""
- 난이도: 실버4
- 분류: 문자열, 수학

요약
- 30의 배수가 되려면 3의 배수이면서 10의 배수여야 한다.
    - 0이 없다면 10의 배수가 될 수 없다.
    - 각 자리 숫자를 더해서 3의 배수가 아니라면 전체 숫자도 3의 배수가 아니다.
- 3의 배수이면서 10의 배수를 만족한다면, 문자열을 역순으로 정렬하면 끝.
"""
