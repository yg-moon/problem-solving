# 햄버거 분배
N, K = map(int, input().split())
data = list(input())

answer = 0

for i in range(N):
    if data[i] == "P":
        for j in range(max(i - K, 0), min(i + K + 1, N)):  # 팁1: 범위 간단하게 처리
            if data[j] == "H":
                data[j] = "E"  # 팁2: 먹었음 표시
                answer += 1
                break

print(answer)

"""
- 난이도: 실버3
- 분류: 그리디

핵심
- 사람의 위치에서 양쪽으로 +/- k범위에서 '가장 왼쪽에 있는' 햄버거를 고르기
- 이유: '뒷사람은 왼쪽에서만 햄버거를 찾아야하기 때문'에 최대한 오른쪽에 있는 것들을 먹지 않아야 함
"""
