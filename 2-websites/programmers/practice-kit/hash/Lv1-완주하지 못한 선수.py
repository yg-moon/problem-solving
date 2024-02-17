from collections import Counter


def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    # 해당 이름의 카운터 값이 다를 경우 정답
    for name in participant_counter:
        if participant_counter[name] != completion_counter[name]:
            return name
