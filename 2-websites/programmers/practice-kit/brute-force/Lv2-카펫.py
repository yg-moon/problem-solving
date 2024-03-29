def solution(brown, yellow):
    area = brown + yellow

    # w * h = 전체 넓이인 모든 경우에서, (w-2) * (h-2) = yellow를 만족하면 정답. (단, w >= h)
    for i in range(3, int(area**0.5) + 1):
        if area % i == 0:
            height = i
            width = area // i
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
