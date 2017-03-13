"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
Example :

Given the following binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
 Note 1: that using recursion has memory over
"""


def next_right_pointer(root):
    cur_level = [root]
    while cur_level:
        next_level = []
        for node in cur_level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        cur_level = next_level
        for index, node in enumerate(next_level):
            if index+1 != len(next_level):
                node.next = next_level[index+1]


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    # arr = [3, 9, 20, None, None, 15, 7]
    inp = """621367 400139 986434 318453 562082 727076 -1 208016 340383 409269
    -1 702531 983736 187691 -1 -1 387077 -1 534779 647033 719463 824451 -1 -1
    -1 373900 -1 517606 -1 -1 -1 -1 720965 -1 834145 -1 -1 -1 -1 -1 -1 -1 -1"""
    arr = []
    for ele in inp.split(" "):
        if ele != -1:
            arr.append(ele)
        else:
            arr.append(None)
    # arr = [1, 2, 3, 4, 5, 6, 7]
    root = level_order_array_to_tree(arr)
    next_right_pointer(root)
    import ipdb
    ipdb.set_trace()
    while root:
        if root.left:
            cur_root = root.left
            root = root.left
        else:
            cur_root = root.right
            root = root.right
        while cur_root is not None:
            print cur_root.val
            cur_root = cur_root.next
