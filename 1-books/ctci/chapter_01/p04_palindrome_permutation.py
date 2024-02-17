# O(N)
import string
import unittest
from collections import Counter


def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]


def is_palindrome_permutation(phrase):
    """checks if a string is a permutation of a palindrome"""
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1


def char_number(c):
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a

    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1


def is_palindrome_bit_vector(phrase):
    """checks if a string is a permutation of a palindrome"""
    res = 0
    for c in clean_phrase(phrase):
        val = ord(c)
        mask = 1 << val
        if res & mask:
            res &= ~mask
        else:
            res |= mask
    return (res - 1) & res == 0


def is_palindrome_bit_vector2(phrase):
    """checks if a string is a permutation of a palindrome using XOR operation"""
    count_odd = 0
    for c in phrase:
        val = char_number(c)
        if val == -1:
            continue
        count_odd ^= 1 << val

    return count_odd & count_odd - 1 == 0


def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(clean_phrase(phrase))
    return sum(val % 2 for val in counter.values()) <= 1


def my_sol(s):
    # 소문자 알파벳만 남기기
    new_s = ""
    s = s.lower()
    for char in s:
        if char.isalpha():
            new_s += char

    # 각 문자의 개수 세기
    dic = {}
    for char in new_s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    # 전체길이가 짝수인 경우, 모든 문자의 개수가 짝수여야 함
    if len(new_s) % 2 == 0:
        for key in dic:
            if dic[key] % 2 != 0:
                return False
        return True

    # 전체길이가 홀수인 경우, 한 문자의 개수만 홀수여야 함
    cnt = 0
    if len(new_s) % 2 != 0:
        for key in dic:
            if dic[key] % 2 != 0:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        is_palindrome_permutation,
        is_palindrome_bit_vector,
        is_palindrome_permutation_pythonic,
        is_palindrome_bit_vector2,
        my_sol,
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
