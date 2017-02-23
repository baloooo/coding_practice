class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


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
