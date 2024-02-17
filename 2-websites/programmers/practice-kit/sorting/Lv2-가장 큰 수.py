def solution(numbers):
    str_nums = [str(num) for num in numbers]
    str_nums.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(str_nums)))


"""
- number는 1000 이하의 숫자이므로, 세자리수로 늘려놓고 사전순 정렬하면 된다는 발상
"""
