from collections import defaultdict


def solution(genres, plays):
    genre_to_plays = defaultdict(int)  # {장르: 총 재생횟수}
    genre_to_info = defaultdict(list)  # {장르: [[고유번호1, 재생횟수1], ...]}

    for i in range(len(genres)):
        genre_to_plays[genres[i]] += plays[i]
        genre_to_info[genres[i]].append([i, plays[i]])

    # 리스트로 변환하고, 총 재생횟수 기준으로 정렬
    list_gtp = list(genre_to_plays.items())
    list_gtp.sort(key=lambda x: x[1], reverse=True)

    # 장르별 곡 목록을 재생횟수 기준으로 정렬
    for genre in genre_to_info:
        genre_to_info[genre].sort(key=lambda x: x[1], reverse=True)

    # 장르별 최대 2개의 곡까지만 수록
    answer = []
    for genre, _ in list_gtp:
        cnt = 2
        if len(genre_to_info[genre]) == 1:
            cnt = 1
        for i in range(cnt):
            answer.append(genre_to_info[genre][i][0])
    return answer


"""
- {장르: 재생횟수} -> list로 변환해서 sort 후 앞에서부터 하나씩 반복.
- {장르: [[고유번호1, 재생횟수1], ...]} -> sort 후 최대 2개까지 수록.
"""
