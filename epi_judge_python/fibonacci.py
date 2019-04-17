from test_framework import generic_test


def fibonacci(n):
    if n == 0:
        return 0

    r = [0] * (n+1)
    r[0] = 0
    r[1] = 1
    if n > 1:
        for i in range(2, n+1):
            r[i] = r[i-1] + r[i-2]

    return r[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
