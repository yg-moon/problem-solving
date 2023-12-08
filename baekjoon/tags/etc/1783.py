# 병든 나이트
N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M + 1) // 2))
elif M <= 6:
    print(min(4, M))
else:
    print(M - 2)

"""
- 난이도: 실버3
- 분류: 그리디, 많은 조건 분기

- 요약: 경우의 수 노가다 (N과 M의 제한에 따라 보이는 패턴찾기)
- 팁: 제약사항이 지나치게 클 경우, 경우의 수가 한정된 그리디 풀이도 고려하자
- 출처: https://afterdawncoding.tistory.com/202
"""
