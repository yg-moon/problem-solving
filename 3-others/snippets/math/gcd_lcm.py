def gcd(a, b):
    # Euclidean algorithm (iterative)
    while b != 0:
        a, b = b, a % b
    return a


def gcd_2(a, b):
    # Euclidean algorithm (recursive)
    if a % b == 0:
        return b
    return gcd_2(b, a % b)


def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm


def manual_lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1

    return lcm
