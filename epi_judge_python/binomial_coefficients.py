from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    """Key insight: n things k at a time is equivalent to
       (n-1) things k at a time plus (n-1) things (k-1) at a time"""
    g = [[0 for _ in range(k+1)] for _ in range(n+1)]
    g[0][0] = 1
    for i in range(1, n+1):
        # special case: only one way to select the 0th element
        g[i][0] = 1
        for j in range(1, k+1):
            if j > i:
                break
            # (n k) = ((n-1) k) + ((n-1) (k-1))
            g[i][j] = g[i-1][j] + g[i-1][j-1]
    return g[n][k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
