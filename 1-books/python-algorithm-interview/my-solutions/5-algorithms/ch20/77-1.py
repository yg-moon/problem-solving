from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left = right = 0

        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1

            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counter.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counter[s[left]] -= 1
                left += 1

        return right - left
