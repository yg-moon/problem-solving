from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)  # 각 글자당 필요한 개수
        missing = len(t)  # 필요한 전체 글자의 개수
        left = start = end = 0

        # right를 한칸씩 이동하며 나아감
        for right, char in enumerate(s, 1):
            if required[char] > 0:
                missing -= 1
            required[char] -= 1

            # missing == 0 이면 left를 이동
            if missing == 0:
                # 일단 카운터 값이 0이 아닌 문자가 나올때까지 left를 이동
                while left < right and required[s[left]] < 0:
                    required[s[left]] += 1
                    left += 1

                # 지금 찾은게 더 짧으면 정답을 갱신
                if not end or right - left <= end - start:
                    start, end = left, right

                # left를 한칸 우측으로 이동하여 다음 윈도우 확인
                required[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
