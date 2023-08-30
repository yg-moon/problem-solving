# 출처: https://ggarden.tistory.com/entry/백준-1057-토너먼트-Python
N, A, B = map(int, input().split())
rounds = 0

while A != B:
    A -= A // 2
    B -= B // 2
    rounds += 1

print(rounds)

"""
- 난이도: 실버4
- 분류: 수학

- 설명
N = 8 일 때
각 팀 1 2 3 4 5 6 7 8 을
묶음  1 1 2 2 3 3 4 4 로 만드는 방법은?

각 번호를 2로 나눈 몫을 빼주면 된다
그리고 결과가 다르면 계속 반복

1 1 2 2 3 3 4 4 1차 가공
1 1 1 1 2 2 2 2 2차 가공
1 1 1 1 1 1 1 1 3차 가공
3차 가공하면 토너먼트 종료
"""
