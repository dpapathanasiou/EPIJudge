from test_framework import generic_test


def search_first_of_k(A, k):
    left  = 0
    right = len(A) - 1
    match = -1
    while left <= right:
        m = (left + right) // 2
        if A[m] > k:
            right = m - 1
        elif A[m] == k:
            # match found, but keep looking leftwards for the first one (if this is not it)
            match = m
            right = m - 1
        else:
            left = m + 1
    return match


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
