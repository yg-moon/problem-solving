def solution(answers):
    # 각 수포자들 찍는 패턴에 따른 배열 만들기
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # % 연산자를 이용해서 각 수포자가 몇 개 맞췄는지 계산
    def solve(person):
        correct = 0
        length = len(person)
        for i in range(len(answers)):
            if answers[i] == person[i % length]:
                correct += 1
        return correct

    # 최고점인 사람들을 출력
    score = [solve(person_1), solve(person_2), solve(person_3)]
    answer = []
    for i in range(3):
        if score[i] == max(score):
            answer.append(i + 1)
    return answer
