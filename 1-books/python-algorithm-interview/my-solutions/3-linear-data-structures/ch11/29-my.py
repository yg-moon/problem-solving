class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_list = [j for j in jewels]
        count = 0

        for stone in stones:
            if stone in jewel_list:
                count += 1
        return count
