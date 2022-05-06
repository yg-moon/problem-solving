from collections import Counter


def solution(participant, completion):
    answer = ''
    part_counter = Counter(participant)
    comp_counter = Counter(completion)

    for name in part_counter:
        if name not in comp_counter or part_counter[name] != comp_counter[name]:
            answer = name
 
    return answer
