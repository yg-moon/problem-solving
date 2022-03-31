# Time Limited Exceeded in case 10C4.

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        prev_elements = []
        seen_sets = []

        def dfs(elements):
            # Add to result when length matches
            if len(prev_elements) == k and set(prev_elements) not in seen_sets:
                prev_elements_copied = prev_elements[:]
                results.append(prev_elements_copied)
                seen_sets.append(set(prev_elements_copied))
                return

            # Generate combinations
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs([x for x in range(1, n+1)])
        return results
