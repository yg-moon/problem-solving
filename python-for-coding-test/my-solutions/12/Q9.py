# Kakao 2020
def solution(s):
    min_len = len(s)

    # 압축 단위: 문자열 길이 절반까지만 확인
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        start = 0
        while start < len(s):
            substr = s[start : start + i]
            next = start + i
            cnt = 1
            # 일치하면 다음 범위까지 확인
            while substr == s[next : next + i]:
                cnt += 1
                next = next + i
            start = next
            # 압축 문자열에 추가
            if cnt > 1:
                compressed += str(cnt)
            compressed += substr
        # 최소 길이 기록
        if len(compressed) < min_len:
            min_len = len(compressed)

    return min_len
