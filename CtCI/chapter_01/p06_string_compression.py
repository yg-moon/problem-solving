import time
import unittest


def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)


def my_sol(s):
    # 예외처리: 빈 문자열
    if not s:
        return s

    res = ""
    prev = s[0]
    cnt = 1

    for char in s[1:]:
        if char == prev:
            cnt += 1
        else:
            res += prev
            res += str(cnt)
            cnt = 1
            prev = char

    # 주의: 끝부분 누락하지 말기
    res += prev
    res += str(cnt)

    if len(res) >= len(s):
        return s
    return res


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [compress_string, my_sol]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected, (
                        test_string,
                        f(test_string),
                        expected,
                    )
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
