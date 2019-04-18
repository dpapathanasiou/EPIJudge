from test_framework import generic_test


def binary_search(lst, elem):
    """Is elem in the list?"""

    l = len(lst)
    if l == 0:
        return False

    m = l // 2
    if lst[m] == elem:
        return True
    elif elem < lst[m]:
        return binary_search(lst[:m], elem)
    else:
        return binary_search(lst[m+1:], elem)

def intersect_two_sorted_arrays(A, B):
    #return sorted(set(A) & set(B))

    if len(A) < len(B):
        return sorted(set([x for x in list(set(A)) if binary_search(B, x)]))
    return sorted(set([x for x in list(set(B)) if binary_search(A, x)]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
