import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            # idle 개수 계산을 위한 변수
            sub_count = 0

            # max heap 처럼, 가장 많은 것부터 추출
            # n이 아닌 n+1 까지하여 예외처리 생략
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                counter.subtract(task)
                # 개수가 0인 아이템을 목록에서 제거
                if counter[task] == 0:
                    del counter[task]

            # idle 계산 전에 멈춰야 맨 뒤에 불필요한 idle이 들어가지 않는다.
            if not counter:
                break

            # idle 개수 계산
            result += n - sub_count + 1

        return result
