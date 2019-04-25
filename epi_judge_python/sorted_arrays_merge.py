from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays):
    heap = []
    for arr in sorted_arrays:
        for i in arr:
            heapq.heappush(heap, i)
    return [heapq.heappop(heap) for _ in range(len(heap))]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
