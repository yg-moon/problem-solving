from collections import defaultdict


def solution(gems):
    gems_set = set(gems)
    gem_cnt_dict = defaultdict(int)
    l = 0
    r = 0
    l_res = l
    r_res = len(gems)
    min_len = len(gems)

    while r < len(gems):
        # 윈도우 우측 확장
        gem_cnt_dict[gems[r]] += 1
        r += 1

        # 핵심: 해시맵의 길이(키의 개수)로 비교
        while len(gem_cnt_dict) == len(gems_set):
            # 조건이 맞으면 답을 저장
            if r - l < min_len:
                min_len = r - l
                l_res = l
                r_res = r

            # 윈도우 좌측 축소
            gem_cnt_dict[gems[l]] -= 1
            # 주의: 카운트가 0이 되면 완전히 제거
            if gem_cnt_dict[gems[l]] == 0:
                del gem_cnt_dict[gems[l]]
            l += 1

    return [l_res + 1, r_res]


"""
- 분류: 투포인터 (슬라이딩 윈도우)
"""
