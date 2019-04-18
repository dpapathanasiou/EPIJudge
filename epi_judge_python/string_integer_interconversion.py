from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    if x == 0:
        return '0'

    neg = x < 0
    x = abs(x)

    chars = []
    while x > 0:
        rem = x % 10
        chars.insert(0, '%d' % rem) # irony!
        x = x // 10

    if neg:
        chars.insert(0, '-')

    return ''.join(chars)

def get_digit (c):
    for i in range(10):
        if c == chr(ord('0')+i):
            return i
    raise ValueError("char is not a digit")

def string_to_int(s):
    if len(s) == 0:
        raise ValueError("invalid input")

    neg = s[0] == '-'
    if neg:
        s = s[1:]

    i = 0
    for j in range(len(s)):
        i += get_digit(s[j]) * (10 ** (len(s)-j-1))

    if neg:
         i = -1 * i

    return i


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
