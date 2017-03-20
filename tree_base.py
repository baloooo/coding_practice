# -*- coding: utf-8
class Node:
    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{0} -> {1}".format(self.val, self.next)

    def __init__(self, x):
        self.left = None
        self.right = None
        self.next = None
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

def construct_tree_from_levelorder_inorder(inorder, levelorder):
    pass


def level_order_array_to_tree(arr):
    """
    Tree will be constructed in a row major order from the arr with
    None depicting absence of nodes.
    [100, 50, 150, inf, 75, 125, inf]
                100
               /   \
             50    150
            / \    /  \
          inf  75 125 inf
    Note: It has to be complete binary tree like above example.
                100
                  \
                  150
                    \
                    175
    won't work.
    """
    node_object_list = [False]*len(arr)
    for index, ele in enumerate(arr):
        if ele is None:
            continue
        if isinstance(node_object_list[index], Node):
            cur_node = node_object_list[index]
        elif not node_object_list[index]:
            cur_node = Node(ele)
            node_object_list[index] = cur_node
        else:
            continue
        for i in range(1, 3):
            if 2*index+i > (len(arr)-1):
                # left child of cur_node out of bounds.
                break
            if arr[2*index+i] is None:
                # subsituting node_obj_list with boolean instead of more descriptive val to preserve space.
                node_object_list[2*index+i] = True
            else:
                child_node = Node(arr[2*index+i])
                if i % 2:
                    cur_node.left = child_node
                else:
                    cur_node.right = child_node
                node_object_list[2*index+i] = child_node
        # if 2*index+2 > (len(arr)-1):
        #     break
        # if arr[2*index+2] is None:
        #     node_object_list[2*index+2] = True
        # else:
        #     right_node = Node(arr[2*index+2])
        #     cur_node.right = right_node
        #     node_object_list[2*index+2] = right_node
    return node_object_list[0]

if __name__ == '__main__':
    arr = [1, 2, 3, None, None, 4, None, None, 5]
    arr = [100, None, 150, None, 175]
    root = level_order_array_to_tree(arr) 
    print_tree_dfs(root)
    import ipdb; ipdb.set_trace()
