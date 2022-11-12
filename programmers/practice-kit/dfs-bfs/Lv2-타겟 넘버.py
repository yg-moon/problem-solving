def solution(numbers, target):
    N = len(numbers)
    cnt = 0

    def dfs(res, idx):
        if idx == N:
            if res == target:
                nonlocal cnt
                cnt += 1
            return
        dfs(res + numbers[idx], idx + 1)
        dfs(res - numbers[idx], idx + 1)

    dfs(0, 0)
    return cnt


"""
- 요약: DFS 완전탐색
- 구현
    - 앞에서부터 모든 수에 +와 -를 붙여보면서 끝까지 계산.
    - 끝까지 왔을때 결과값이 타겟과 같으면 카운트 1 증가.
"""
