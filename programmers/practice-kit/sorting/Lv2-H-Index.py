def solution(citations):
    citations.sort(reverse=True)

    # 예외 처리: 배열의 마지막 원소 > 배열 전체길이 이면 h_idx의 초기값을 배열의 전체길이로 설정.
    # 처음엔 h_idx의 초기값을 항상 0으로 설정했는데, [4,4,4] 라는 반례가 있다.
    if citations[len(citations) - 1] > len(citations):
        h_idx = len(citations)
    else:
        h_idx = 0

    # 핵심: 역순으로 정렬하고, i번째 원소 ≤ i 이면 h_idx = max(i번째 원소, i-1) 설정 후 break
    # 직접 예제를 놓고 생각하면 쉽게 알 수 있다.
    for i in range(len(citations)):
        if citations[i] <= i + 1:
            h_idx = max(citations[i], i)
            break
    return h_idx
