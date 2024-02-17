# BOJ 1759
from itertools import combinations

L, C = map(int, input().split())
letters = list(input().split())

vowels = []
consonants = []
for l in letters:
    if l in ["a", "e", "i", "o", "u"]:
        vowels.append(l)
    else:
        consonants.append(l)

two_consonant_comb = list(combinations(consonants, 2))
result = set()


def get_L():
    return L


# 모음 하나 마다
for v in vowels:
    pw1 = v
    # 자음 두개의 조합 전부 붙여보고
    for tsc in two_consonant_comb:
        pw2 = pw1 + "".join(tsc)
        used = [v, tsc[0], tsc[1]]
        other_letters = [x for x in letters if x not in used]
        other_letters_comb = list(combinations(other_letters, get_L() - 3))
        # 전체에서 그 세글자를 뺀 나머지 글자의 조합으로 완성
        for olc in other_letters_comb:
            pw3 = pw2 + "".join(olc)
            result.add("".join(sorted(pw3)))

for r in sorted(result):
    print(r)
