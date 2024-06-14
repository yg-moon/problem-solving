N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))


def dfs(idx, health, joy):
    # base case
    if health <= 0:
        return -int(1e9)
    if idx >= N:
        return joy

    # 중간 변수
    option1 = dfs(idx + 1, health - L[idx], joy + J[idx])
    option2 = dfs(idx + 1, health, joy)

    # 기본 리턴값
    return max(option1, option2)


print(dfs(0, 100, 0))

"""
- 나는 끝에 도달했을 경우 전역변수의 값을 업데이트 하는 방법만 사용했는데,
  이렇게 리턴값을 사용하는 방식도 배워두면 좋을 것 같다.
"""
