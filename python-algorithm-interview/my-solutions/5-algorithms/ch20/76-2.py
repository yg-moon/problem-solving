import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= (need[char] > 0)
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # 이번에 찾은게 더 짧으면 갱신
                if not end or right - left <= end - start:
                    start, end = left, right

                # 다음 탐색을 위해 값 복구
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
