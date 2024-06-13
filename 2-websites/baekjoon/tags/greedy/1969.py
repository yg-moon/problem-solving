# DNA
from collections import defaultdict

N, M = map(int, input().split())
arr = [defaultdict(int) for _ in range(M)]  # 각 자릿수마다 알파벳의 개수
dna_lst = []

for _ in range(N):
    dna = input()
    dna_lst.append(dna)
    for i in range(M):
        arr[i][dna[i]] += 1

# 각 자리별 알파벳 선정
result = []
for dic in arr:
    char = sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0]
    result.append(char)
answer = "".join(result)

# 해밍거리 계산
cnt = 0
for dna in dna_lst:
    for i in range(M):
        if dna[i] != answer[i]:
            cnt += 1

print(answer)
print(cnt)

"""
- 난이도: 실버4
- 분류: 그리디

핵심
- 각 위치에 대해 글자의 개수를 세기
- 가장 개수가 많은 것 / 알파벳 순을 기준으로 정렬해서 하나만 고르기

1-pass
- 각 자릿수에 대해 최종 알파벳과 해밍거리를 계산하면 원패스로 가능
- 참고: https://velog.io/@0sunset0/백준-파이썬-1969-DNA
"""
