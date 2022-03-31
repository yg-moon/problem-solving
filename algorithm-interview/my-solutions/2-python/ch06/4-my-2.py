import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 소문자로 만들고, 특수문자 지우고, 리스트에 저장하기
        lowercase_words = re.sub("[^a-z]", " ", paragraph.lower()).split()
        
        # banned에 있는 것은 리스트에서 제외하기
        unbanned_words = [word for word in lowercase_words if word not in banned]
        
        # 카운트 세기
        return Counter(unbanned_words).most_common(1)[0][0]
