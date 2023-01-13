from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0

        for d in data:
            seq = bin(d)[2:].zfill(8)
            if cnt == 0:
                if seq[0] == "0":
                    continue
                elif seq[0:3] == "110":
                    cnt = 1
                elif seq[0:4] == "1110":
                    cnt = 2
                elif seq[0:5] == "11110":
                    cnt = 3
                else:
                    return False
            # 남은 cnt 개수만큼 "10"으로 시작하는 시퀀스가 반복되어야함
            else:
                if seq[0:2] == "10":
                    cnt -= 1
                else:
                    return False

        # 끝나고 cnt가 남아있으면 안 됨
        return cnt == 0
