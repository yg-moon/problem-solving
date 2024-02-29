from typing import List


class Solution:
    # 방법1. 구현
    # 공간복잡도 O(N)
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        prev = chars[0]
        cnt = 1
        lst = []

        # 핵심: 이전 글자와 다른지 확인
        for i in range(1, len(chars)):
            cur = chars[i]
            if prev == cur:
                cnt += 1
            else:
                if cnt == 1:
                    lst.append(prev)
                else:
                    lst.append(prev)
                    # 주의: 숫자는 한글자씩 끊어서 넣기
                    for x in str(cnt):
                        lst.append(x)
                cnt = 1
            prev = cur

        # 마지막에 남은거
        if cnt == 1:
            lst.append(prev)
        else:
            lst.append(prev)
            for x in str(cnt):
                lst.append(x)

        # 원본 문자열 변경
        for i in range(len(lst)):
            chars[i] = lst[i]

        return len(lst)

    # Sol. 투포인터
    # 공간복잡도 O(1)
    def compress(self, chars: List[str]) -> int:
        i = 0  # 문자열을 훑을 포인터1
        answer = 0  # 정답을 작성할 포인터2

        while i < len(chars):
            cur = chars[i]
            cnt = 0

            # 카운트 올리기
            while i < len(chars) and chars[i] == cur:
                cnt += 1
                i += 1

            # 문자 작성
            chars[answer] = cur
            answer += 1

            # 숫자 작성
            if cnt > 1:
                for c in str(cnt):
                    chars[answer] = c
                    answer += 1

        return answer


"""
- 난이도: Medium
- 분류: 구현, 투포인터
"""
