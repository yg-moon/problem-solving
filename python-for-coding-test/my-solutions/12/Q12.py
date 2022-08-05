# Kakao 2020
# 출처: 이코테

# 현재 설치된 구조물들이 모두 조건을 만족하는지 확인
def valid(answer):
    for x, y, material in answer:
        # 기둥
        if material == 0:
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if (
                y == 0
                or [x - 1, y, 1] in answer  # 한 칸 왼쪽에서 시작하는 보가 있음
                or [x, y, 1] in answer  # 현 위치에서 시작하는 보가 있음
                or [x, y - 1, 0] in answer
            ):
                continue
            return False
        # 보
        elif material == 1:
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if (
                [x, y - 1, 0] in answer
                or [x + 1, y - 1, 0] in answer
                or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)
            ):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, material, op = frame
        # 삭제
        if op == 0:
            # 일단 삭제를 해본 뒤에, 가능한 구조물이 아니라면 다시 설치
            answer.remove([x, y, material])
            if not valid(answer):
                answer.append([x, y, material])
        # 설치
        if op == 1:
            answer.append([x, y, material])
            if not valid(answer):
                answer.remove([x, y, material])
    answer.sort()
    return answer
