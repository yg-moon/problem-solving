def solution(citations):
    # 역순 정렬
    citations.sort(reverse=True)

    # 예외 처리
    # 마지막 원소 > 배열의 길이면 h_idx의 초기값을 배열의 길이로 설정
    if citations[len(citations) - 1] > len(citations):
        h_idx = len(citations)
    else:
        h_idx = 0

    # 핵심
    # i번째 원소 ≤ i+1 이면 h_idx = max(i번째 원소, i) 설정 후 break
    for i in range(len(citations)):
        if citations[i] <= i + 1:
            h_idx = max(citations[i], i)
            break
    return h_idx
