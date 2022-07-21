# Kakao 2020
# from 이코테

from itertools import permutations

def solution(n, weak, dist):
    # 원본 길이 저장
    weak_len = len(weak)
    
    # 원형구조 처리: 길이를 2배로 늘려서 일자로 변형
    for i in range(weak_len):
        weak.append(weak[i] + n)

    # 정답: 투입할 친구 수의 최솟값
    answer = len(dist) + 1

    # 핵심: 취약점 배열 weak에 대해, 늘리기 전 길이까지만 시작점으로 잡고 순회.
    for start in range(weak_len):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            # 투입할 친구의 수
            cnt = 1
            # 지금 친구가 점검할 수 있는 마지막 위치
            last = weak[start] + friends[cnt - 1]
            # 시작점부터 모든 취약점을 확인
            for idx in range(start, start + weak_len):
                # 점검할 수 있는 위치를 벗어나는 경우
                if last < weak[idx]:
                    # 새로운 친구를 투입
                    cnt += 1
                    # 더 투입이 불가능하다면 종료
                    if cnt > len(dist):
                        break
                    # 마지막 위치 업데이트
                    last = weak[idx] + friends[cnt - 1]
            answer = min(answer, cnt)

    # 필요한 친구 수가 전체 친구 수보다 많다면, 점검 불가능.
    if answer > len(dist):
        return -1
    return answer
