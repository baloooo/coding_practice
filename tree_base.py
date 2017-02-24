# -*- coding: utf-8
class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


def print_tree_dfs(root):
    if root is None:
        return
    print root.val
    print_tree_dfs(root.left)
    print_tree_dfs(root.right)


def array_to_tree(arr):
    """
    Given an array that represents a tree in such a way that array indexes are
    values in tree nodes and array values give the parent node of that
    particular index (or node). The value of the root node index would always
    be -1 as there is no parent for root. Construct the standard linked
    representation of given Binary Tree from this given representation.
    Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
    Output:
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6
    """
    node_map = {}
    root = None
    for index, ele in enumerate(arr):
        if node_map.get(index) is None:
            cur_node = Node(index)
        else:
            cur_node = node_map[index]
        node_map[index] = cur_node
        if ele == -1:
            root = cur_node
            continue
        if node_map.get(ele) is None:
            node_map[ele] = Node(ele)
        if node_map[ele].left is None:
            node_map[ele].left = cur_node
        else:
            node_map[ele].right = cur_node
    return root


def construct_tree_from_array(arr):
    """
    Tree will be constructed in a row major order from the arr with
    float('inf') depicting absence of nodes.
    [100, 50, 150, inf, 75, 125, inf]
                100
               /   \
             50    150
            / \    /  \
          inf  75 125 inf

    """
    head = root = Node(arr[0])
    for index, ele in enumerate(arr[1:]):
        cur_node = Node(ele)
        if index % 2 == 0:
            root.left = cur_node
        else:
            root.right = cur_node
            if root.left.val != float('inf'):
                root = root.left
            else:
                root = root.right
    return head
