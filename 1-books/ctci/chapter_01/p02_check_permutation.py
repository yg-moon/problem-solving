# O(N)
import unittest
from collections import Counter


def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True


def check_permutation_pythonic(str1, str2):
    # short-circuit to avoid instantiating a Counter which for big strings
    # may be an expensive operation
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


def my_sol(s1, s2):
    # 예외처리
    if len(s1) != len(s2) or s1 == s2:
        return False

    dic = {}
    for char in s1:
        if char not in dic:
            dic[char] = 1
        dic[char] += 1
    for char in s2:
        if char not in dic or dic[char] == 0:
            return False
        dic[char] -= 1
    return True


def my_sol2(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return False

    if sorted(s1) == sorted(s2):
        return True
    return False


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
        my_sol,
        my_sol2,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
