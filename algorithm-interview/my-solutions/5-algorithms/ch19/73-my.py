from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for d in data:
            seq = bin(d)[2:].zfill(8)

            # count 개수 만큼 '10' 패턴이 나오는지 확인
            if count > 0:
                if seq[0:2] != "10":
                    return False
                count -= 1
                continue

            # 잘못된 경우
            if int(seq, 2) >= 0xF8 or seq[0:2] == "10":
                return False

            # 패턴에 따라 count 올리기
            if seq[0:5] == "11110":
                count = 3
            elif seq[0:4] == "1110":
                count = 2
            elif seq[0:3] == "110":
                count = 1

        # 끝났는데 count가 남아있는 경우
        if count > 0:
            return False

        # 다른 경우는 상관없음
        return True
