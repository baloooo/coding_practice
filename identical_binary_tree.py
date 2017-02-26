"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 or True
"""
def are_identical(root1, root2):
    if root1 is None or root2 is None:
        if root1 != root2:
            return False
        else:
            return True
    if root1.val != root2.val:
        return False
    if not are_identical(root1.left, root2.left):
        return False
    if not are_identical(root1.right, root2.right):
        return False
    return True


if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    # arr1, arr2 = [1, 2, 3], [1, 2, 3]
    # arr1, arr2 = [1, 2, 3], [1, None, 2, None, 3]
    # arr1, arr2 = [1, 2, None], [1, None, 2]
    # arr1, arr2 = [1, 2, 3], [1, 3, 2]
    # arr1, arr2 = [4, 2, 3], [1, 2, 3]
    # arr1, arr2 = [1, 2, 3], [1, 2, None]
    arr1, arr2 = [1], [1]
    root1 = level_order_array_to_tree(arr1)
    root2 = level_order_array_to_tree(arr2)
    print are_identical(root1, root2)
