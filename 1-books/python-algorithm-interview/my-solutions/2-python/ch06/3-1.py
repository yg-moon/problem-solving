from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        # Separate logs into two lists
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # Sort letters list by first by content, then by identifier
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits


### Time Complexity
# for문은 O(n), 정렬은 O(nlogn) 이지만, 글자 길이 제한 때문에 사실상 정렬은 O(1) 이므로
# 전체는 O(n).

### Note
# Corner Case: 인풋이 조건에 맞게 주어진다면 따로 고려할게 없음.
