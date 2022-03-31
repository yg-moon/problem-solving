import re
from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_to_count = defaultdict(int)

        # Remove symbols & convert to lowercase
        filtered_words = re.sub('[^a-z]', ' ', paragraph.lower()).split()

        # Increase count for each word
        for word in filtered_words:
            if word not in banned:
                word_to_count[word] += 1
        
        # Find the most frequent word
        most_common_word = ''
        max_count = 0
        for word in word_to_count:
            if word_to_count[word] > max_count:
                most_common_word = word
                max_count = word_to_count[word]

        return most_common_word


### Time Complexity
# O(n)

### Note
# Counter를 쓰지 않고 dict만을 써서 해결했다.
