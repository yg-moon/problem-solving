# 육십갑자 정보를 출력하는 프로그램
gan = "갑을병정무기경신임계"
ji = "자축인묘진사오미신유술해"

colors = ["푸른", "붉은", "노란", "흰", "검은"]
animals = [
    "쥐",
    "소",
    "호랑이",
    "토끼",
    "용",
    "뱀",
    "말",
    "양",
    "원숭이",
    "닭",
    "개",
    "돼지",
]

result = []
i = 0

while True:
    cur = []
    name = gan[i % 10] + ji[i % 12]

    idx = i % 10
    if idx % 2 != 0:
        idx -= 1
    idx //= 2

    meaning = colors[idx] + " " + animals[i % 12]

    cur.append(name)
    cur.append(meaning)

    if cur in result:
        break

    result.append(cur)
    i += 1

year = 1984
for name, meaning in result:
    print(f"{year} {name}년: {meaning}의 해")
    year += 1
