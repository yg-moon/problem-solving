def solution(s):
    min_str = s

    # 모든 단위길이에 대해 압축시도
    for unit in range(1, len(s) + 1):
        compressed = ""
        i = 0
        # 현재 문자열이 끝날 때까지 진행
        while i < len(s):
            chunk = s[i : i + unit]
            cnt = 1
            # 반복표현이 나오는만큼 탐색
            while chunk == s[i + unit : i + unit * 2]:
                i += unit
                cnt += 1
            i += unit
            # 현재 문자열에 추가
            if cnt != 1:
                compressed += str(cnt)
            compressed += chunk
        # 최소 문자열 갱신
        if len(compressed) < len(min_str):
            min_str = compressed

    return len(min_str)


"""
- 모든 문제 읽기: 2:35-2:50 (15분)

- 분류: 구현, 문자열, 완전탐색
- 시간: 2:50-3:20 (30분)
"""
