def solution(commands):
    cells = [[""] * 51 for _ in range(51)]
    merged_sets = []
    result = []

    for command in commands:
        splt = command.split()

        if splt[0] == "UPDATE":
            # "UPDATE r c val"
            if len(splt) == 4:
                r, c, val = splt[1:]
                r = int(r)
                c = int(c)
                for ms in merged_sets:
                    if (r, c) in ms:
                        for mr, mc in ms:
                            cells[mr][mc] = val
                        break
                else:
                    cells[r][c] = val
            # "UPDATE val1 val2"
            elif len(splt) == 3:
                val1, val2 = splt[1:]
                for x in range(51):
                    for y in range(51):
                        if cells[x][y] == val1:
                            cells[x][y] = val2

        elif splt[0] == "MERGE":
            r1, c1, r2, c2 = map(int, splt[1:])
            set1 = None
            set2 = None
            for ms in merged_sets:
                if (r1, c1) in ms:
                    set1 = ms
                if (r2, c2) in ms:
                    set2 = ms

            # 핵심
            if set1 and set2 and set1 == set2:
                continue
            elif not set1 and not set2:
                tmp = set()
                tmp.add((r1, c1))
                tmp.add((r2, c2))
                merged_sets.append(tmp)
                if cells[r1][c1] == "" and cells[r2][c2] != "":
                    cells[r1][c1] = cells[r2][c2]
                else:
                    cells[r2][c2] = cells[r1][c1]
            elif set1 and not set2:
                set1.add((r2, c2))
                if cells[r1][c1] == "" and cells[r2][c2] != "":
                    for mr, mc in set1:
                        cells[mr][mc] = cells[r2][c2]
                else:
                    cells[r2][c2] = cells[r1][c1]
            elif not set1 and set2:
                set2.add((r1, c1))
                if cells[r1][c1] == "" and cells[r2][c2] != "":
                    cells[r1][c1] = cells[r2][c2]
                else:
                    for mr, mc in set2:
                        cells[mr][mc] = cells[r1][c1]
            elif set1 and set2:
                new_set = set1.union(set2)
                merged_sets.append(new_set)
                merged_sets.remove(set1)
                merged_sets.remove(set2)
                if cells[r1][c1] == "" and cells[r2][c2] != "":
                    for mr, mc in set1:
                        cells[mr][mc] = cells[r2][c2]
                else:
                    for mr, mc in set2:
                        cells[mr][mc] = cells[r1][c1]

        elif splt[0] == "UNMERGE":
            r, c = map(int, splt[1:])
            found_set = None
            for ms in merged_sets:
                if (r, c) in ms:
                    found_set = ms
                    val = cells[r][c]
                    for mr, mc in ms:
                        cells[mr][mc] = ""
                    cells[r][c] = val
                    break
            if found_set:
                merged_sets.remove(found_set)

        elif splt[0] == "PRINT":
            r, c = map(int, splt[1:])
            if cells[r][c] == "":
                result.append("EMPTY")
            else:
                result.append(cells[r][c])

        else:
            print("Wrong Command!")

    return result


"""
- 분류: 구현
- 소요 시간:
    11:30-1:30 (2시간) (계획)
    10:30-11:00 (30분) (구현)

필요 동작
- update1: 선택한 셀의 값을 v로 바꿈
- update2: v1의 값을 가진 모든 셀의 값을 v2로 바꿈
- merge: 인접하지 않아도 가능, 값은 v1로 바뀜, 접근시 병합된 쪽으로
- unmerge: 포함된 모든 셀이 초기상태로 돌아감 (병합해제, 값없음)

핵심
- 1. 같은 그룹에 속하는 좌표들을 관리할 방법이 필요
    -> list of sets
        - 문제점: 병합 동작이 너무 복잡함
        - 해결: 일단 구현해보니 돌아감 (...)
- 2. 해당 좌표들로 접근했을때 보여질 값을 관리할 방법이 필요
    -> 배열에 직접 쓰기
"""
