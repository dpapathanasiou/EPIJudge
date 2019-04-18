from test_framework import generic_test

# use `BinaryTreeNode` from binary_tree_node.py

def inorder_traversal(tree):
    nodes = []
    if tree is not None:
        nodes.extend(inorder_traversal(tree.left))
        nodes.append(tree.data)
        nodes.extend(inorder_traversal(tree.right))
    return nodes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
