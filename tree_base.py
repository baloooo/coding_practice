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
    cur_node = Node(arr[0])
    cur_node
