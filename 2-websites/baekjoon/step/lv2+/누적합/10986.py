# 나머지 합
# 출처: https://only-wanna.tistory.com/entry/파이썬-백준-10986번-나머지-합
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# mod[i]: 누적합 배열에서 M으로 나눈 나머지가 i인 원소의 개수
mod = [0] * M
mod[0] = 1  # 첫 원소에 대한 계산이 생략되므로 따로 추가

csum = 0
for a in arr:
    csum += a
    mod[csum % M] += 1

answer = 0
for m in mod:
    answer += m * (m - 1) // 2  # nC2 = n*(n-1)//2
print(answer)

"""
- 난이도: 골드3
- 분류: 누적합

요약
- P[R], P[L-1]을 M으로 나눈 나머지가 같다면, 둘을 빼면 나머지는 0이 되어 M으로 나누어 떨어짐.
- 결국 '누적합을 M으로 나눈 나머지'가 동일한 idx중에서 선택한 nC2를 모두 더한것이 정답.
- ex. arr: [1, 2, 3, 1, 2]
    -> psum: [0, 1, 3, 6, 7, 9]
    -> psum % M: [0, 1, 0, 0, 1, 0]
    -> 나머지별 개수: {0: 4, 1: 2}
    -> (4C2 + 2C2) = (6 + 1) = 7
"""
