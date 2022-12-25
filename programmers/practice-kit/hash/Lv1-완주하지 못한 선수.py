from collections import Counter


def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    for name in participant_counter:
        if participant_counter[name] != completion_counter[name]:
            return name
