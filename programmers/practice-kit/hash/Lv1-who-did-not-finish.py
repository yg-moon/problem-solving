from collections import Counter


def solution(participant, completion):
    answer = ""
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    for name in participant_counter:
        if (
            name not in completion_counter
            or participant_counter[name] != completion_counter[name]
        ):
            answer = name

    return answer
