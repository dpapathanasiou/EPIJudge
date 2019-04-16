from test_framework import generic_test


def find_maximum_subarray(A):
    local_max  = 0
    global_max = 0

    for i in range(len(A)):
        local_max = max(A[i], A[i] + local_max)
        if local_max > global_max:
            global_max = local_max

    return global_max


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
