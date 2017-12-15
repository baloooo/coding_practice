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


def next_right_pointer_optimized(root):
    """
    Space: O(1) Time: O(n)
    Explanation: @mmozum https://discuss.leetcode.com/topic/1106/o-1-space-o-n-complexity-iterative-solution/37
    """
    while root:
        needle = nxt_lvl_head = TreeLinkNode(-1)
        while root:
            if root.left:
                needle.next = root.left
                needle = needle.next
            if root.right:
                needle.next = root.right
                needle = needle.next
            root = root.next # root is None when one level completes.
        # cur level is over, which also means sewing of next level is completed.
        root = nxt_lvl_head.next

def next_right_pointer(root):
    #  Time: O(n), Space: O(width of binary tree)
    if not root: return
        cur_lvl = [root]
    while cur_lvl:
        nxt_lvl = []
        for index, node in enumerate(cur_lvl):
            if node.left:
                nxt_lvl.append(node.left)
            if node.right:
                nxt_lvl.append(node.right)
            if index < len(cur_lvl)-1:
                cur_lvl[index].next = cur_lvl[index+1]
        cur_lvl = nxt_lvl


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    arr = [3, 9, 20, None, None, 15, 7]
    # inp = """621367 400139 986434 318453 562082 727076 -1 208016 340383 409269  # noqa
    # -1 702531 983736 187691 -1 -1 387077 -1 534779 647033 719463 824451 -1 -1
    # -1 373900 -1 517606 -1 -1 -1 -1 720965 -1 834145 -1 -1 -1 -1 -1 -1 -1 -1"""  # noqa
    # inp = """1 2 3 4 5 6 -1 7 8 9 -1 10 11 12 -1 -1 13 -1 14 15 16 17 -1 -1 -1 18 -1 19 -1 -1 -1 -1 20 -1 21 -1 -1 -1 -1 -1 -1 -1 -1"""  # noqa
    # arr = []
    # for ele in inp.split(" "):
    #     if ele != '-1':
    #         arr.append(ele)
    #     else:
    #         arr.append(None)
    # arr = [1, 2, 3, 4, 5, 6, 7]
    root = level_order_array_to_tree(arr)
    next_right_pointer(root)
    while root:
        print root
        root = root.left
