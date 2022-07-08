s = input()

alpha = ""
num = 0
has_int = False # 0만 들어온 경우와 숫자가 없는 경우를 구분하기 위함

for char in s:
    if char.isalpha():
        alpha += char
    else:
        num += int(char)
        has_int = True

# 예외처리: 입력에 숫자가 없는 경우
if num == 0 and not has_int:
    num = ""

print("".join(sorted(alpha)) + str(num))
