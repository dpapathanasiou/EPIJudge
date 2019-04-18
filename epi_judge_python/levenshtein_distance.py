from test_framework import generic_test


def levenshtein_distance(A, B):
    """Minimize 3 possible actions: edit, delete, insert"""

    g = [[i+j for j in range(len(B)+1)] for i in range(len(A)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                g[i][j] = g[i-1][j-1]
            else:
                g[i][j] = 1 + min(g[i-1][j-1], min(g[i-1][j], g[i][j-1]))
                
    return g[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
