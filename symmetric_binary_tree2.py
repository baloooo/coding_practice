"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric. 
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
def symmetrical_tree(root):
    def is_mirror(root1, root2):
        if root1 is None or root2 is None:
            if root1 != root2:
                return False
            else:
                return True
        if root1.val != root2.val:
            return False
        if not is_mirror(root1.left, root2.right):
            return False
        if not is_mirror(root1.right, root2.left):
            return False
        # if everything went well
        return True
    return is_mirror(root.left, root.right)



if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    # arr = [1, 2, 2, None, 3, 3, None]
    arr = [1, 2, 2, 3, None, 3, None]
    # arr = [1, 2, 2, 3, 4, 4, 3]
    root = level_order_array_to_tree(arr)
    print symmetrical_tree(root)
