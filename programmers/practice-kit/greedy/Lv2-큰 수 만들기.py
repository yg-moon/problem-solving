def solution(number, k):
    number = [int(n) for n in number]
    cur_k = k

    for _ in range(k):
        for i in range(len(number) - 1):
            if number[i] < number[i + 1]:
                del number[i]
                cur_k -= 1
                break

    number = number[: len(number) - cur_k]

    return "".join(list(map(str, number)))


"""
- 시간초과

생각
- 어차피 결과의 자릿수는 똑같다.
- 앞자리수가 더 커야 한다.

구현
- 맨 앞에서부터 보면서, 본인보다 큰게 나오면 현재 위치를 삭제 (k번 반복)
- 아직 남은 자리수만큼 뒤에서부터 삭제
"""
