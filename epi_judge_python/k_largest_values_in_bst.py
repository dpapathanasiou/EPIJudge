from test_framework import generic_test, test_utils

def largest_k(tree, k, nodes):
    if len(nodes) == k:
        return nodes
    if not tree:
        return nodes
    nodes = largest_k(tree.right, k, nodes)
    if len(nodes) < k:
        nodes.append(tree.data)
        nodes = largest_k(tree.left, k, nodes)
    return nodes

def find_k_largest_in_bst(tree, k):
    return largest_k(tree, k, [])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
