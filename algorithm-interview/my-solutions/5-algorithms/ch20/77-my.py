import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left = start = end = 0

        for right, char in enumerate(s):
            counter[char] += 1

            # 슬라이딩 윈도우 안에서 k번의 변경 이내로 단일문자열을 만들수 있어야 한다.
            # 따라서 (슬라이딩 윈도우의 길이) - (가장 흔한 문자의 개수) > k 라면, 왼쪽 포인터 이동.
            if (right - left + 1) - counter.most_common(1)[0][1] > k:
                counter[s[left]] -= 1
                left += 1

            # 이번에 찾은게 길면 갱신
            if not end or end - start <= right - left:
                start, end = left, right

        return right - left + 1
