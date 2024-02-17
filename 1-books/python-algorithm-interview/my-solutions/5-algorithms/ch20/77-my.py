from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left = 0

        for right, char in enumerate(s):
            counter[char] += 1

            # 현재 윈도우 안에서 k번의 변경 이내로 단일문자열을 만들수 있어야 한다.
            # 따라서 (윈도우의 길이) - (가장 흔한 문자의 개수) > k 라면, left를 이동
            if (right - left + 1) - counter.most_common(1)[0][1] > k:
                counter[s[left]] -= 1
                left += 1

        return right - left + 1


"""
문제
- 알파벳을 k번만큼 다른걸로 바꿀수 있다.
- 단일 알파벳으로 이루어진 가장 긴 substring의 길이를 구하라.

핵심
- 현재 윈도우 안에서 k번의 변경이내로 단일문자열을 만들수 있어야 한다.
- 즉, (윈도우의 길이) - (가장 흔한 문자의 개수) <= k 여야 한다.
"""
