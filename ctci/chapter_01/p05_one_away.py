# O(N)
import time
import unittest


def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def my_sol(s1, s2):
    # 길이 차이가 1보다 크면 안됨
    if abs(len(s1) - len(s2)) > 1:
        return False

    # s1이 더 짧은 문자열이 되도록
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i = 0
    j = 0
    edited = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            # 이미 수정한 기록이 있으면 안됨
            if edited:
                return False
            edited = True
            # 삽입/삭제의 경우, 짧은 쪽의 포인터를 한칸 내림
            if len(s1) != len(s2):
                i -= 1
        # 항상 두 포인터를 모두 올림
        i += 1
        j += 1
    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [are_one_edit_different, my_sol]

    def test_one_away(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected, (text_a, text_b)
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
