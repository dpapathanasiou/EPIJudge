from test_framework import generic_test, test_utils


def inorder_traversal(tree):
    nodes = []
    if tree is not None:
        nodes.extend(inorder_traversal(tree.left))
        nodes.append(tree.data)
        nodes.extend(inorder_traversal(tree.right))
    return nodes

def find_k_largest_in_bst(tree, k):
    res = []
    nodes = inorder_traversal(tree)
    for i in range(len(nodes)-1, len(nodes)-k-1, -1):
        res.append(nodes[i])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
