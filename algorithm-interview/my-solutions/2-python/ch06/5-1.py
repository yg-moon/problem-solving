from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_words = defaultdict(list)

        # Using the sorted word as key, append each word
        for word in strs:
            key_to_words[''.join(sorted(word))].append(word)

        # Type cast dict_values object to a list object
        return list(key_to_words.values())


### Time Complexity
# for문 안에 정렬이 들어있으나, 문자열 길이 제한으로 정렬이 상수시간 안에 된다.
# 즉 O(n) * O(mlogm) 인데, m: word length <= 100 이므로 전체는 O(n).

### Note
# -
