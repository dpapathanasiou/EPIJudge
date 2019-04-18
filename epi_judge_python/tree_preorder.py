from test_framework import generic_test


def preorder_traversal(tree):
    nodes = []
    if tree is not None:
        nodes.append(tree.data)
        nodes.extend(preorder_traversal(tree.left))
        nodes.extend(preorder_traversal(tree.right))
    return nodes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
