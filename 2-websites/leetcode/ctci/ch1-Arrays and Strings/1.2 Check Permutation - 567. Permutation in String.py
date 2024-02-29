from collections import Counter
from collections import defaultdict


class Solution:
    # 방법1. 나이브
    # 시간복잡도: O((N-M)*M) -> 1102ms
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            if Counter(s2[i : i + len(s1)]) == counter_s1:
                return True

        return False

    # Sol. 슬라이딩 윈도우
    # 시간복잡도: O(N+M) -> 58ms
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = defaultdict(int)
        s2_dic = defaultdict(int)

        for c in s1:
            s1_dic[c] += 1

        l = 0
        r = 0

        while r < len(s2):
            s2_dic[s2[r]] += 1

            if r - l + 1 == len(s1):
                if s1_dic == s2_dic:
                    return True
                s2_dic[s2[l]] -= 1
                if s2_dic[s2[l]] == 0:
                    del s2_dic[s2[l]]
                l += 1

            r += 1

        return False


"""
(어려운 버전)
- 난이도: Medium
- 분류: 해시, 슬라이딩 윈도우

- 비슷한 문제: 카카오 2020 인턴 Q3 '보석 쇼핑'
"""
