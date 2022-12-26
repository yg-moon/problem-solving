def gcd(x, y):
    # Euclidean algorithm
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


def manual_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm
