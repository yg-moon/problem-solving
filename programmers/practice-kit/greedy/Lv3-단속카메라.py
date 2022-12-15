def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = routes[0][1]
    cnt = 1

    for start, end in routes[1:]:
        if start > camera:
            camera = end
            cnt += 1

    return cnt


"""
- 핵심: 카메라는 항상 (진입지점이 아니라) 진출지점에만 설치한다.
- 알고리즘
    - `routes` 배열을 (진입지점이 아니라) 진출지점 기준으로 정렬하고 for문으로 순회
    - `다음 진입지점 ≤ 현재 카메라 위치`이면, 그냥 다음으로 넘어감 (이미 단속할 수 있으므로)
    - `다음 진입지점 > 현재 카메라 위치`이면, 카메라 개수 +1 하고, 카메라를 현재 종점위치로 갱신
"""
