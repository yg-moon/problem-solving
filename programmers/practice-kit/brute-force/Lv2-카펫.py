def solution(brown, yellow):
    # 전체 넓이
    area = brown + yellow

    # w * h = 전체 넓이인 모든 경우에서, (w-2) * (h-2) = yellow를 만족하면 정답.
    for i in range(3, int(area**0.5) + 1):
        if area % i == 0:
            h = i
            w = area // i
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
