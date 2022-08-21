from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        len_cand = len(candidates)

        def dfs(csum, idx, path):
            if csum > target:
                return
            if csum == target:
                result.append(path)
                return

            # 자신부터 하위원소까지 재귀호출
            for i in range(idx, len_cand):
                dfs(csum + candidates[i], i, path + [candidates[i]])

        dfs(0, 0, [])
        return result
