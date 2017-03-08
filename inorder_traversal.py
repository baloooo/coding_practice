# coding:utf-8
"""
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].
"""
def inorder_recursion(root):
    inorder_list = []
    def inorder(root):
        if root is None:
            return 
        inorder(root.left)
        inorder_list.append(root.val)
        inorder(root.right)
    inorder(root)
    return inorder_list

def inorder_iteration(root):
    # trick is to use stack, which recursion uses also.
    from tree_base import Node
    stack = [root]
    tos = None
    in_order = []
    while(stack or tos is not None):
        if tos is None:
            tos = stack.pop()
        if not isinstance(tos, Node):
            in_order.append(tos)
            try:
                tos = stack.pop()
            except IndexError:
                tos = None
            continue
        if tos.right is not None:
            stack.append(tos.right)
        stack.append(tos.val)
        tos = tos.left
    return in_order



if __name__ == '__main__':
    from tree_base import level_order_array_to_tree
    # arr = [1, None, 2, None, None, 3, None]
    # arr = ['A', 'B', 'C', 'D', "E", "F", "G"]
    # arr = ['A', 'B', 'C']
    arr = ['a', 'b']
    root = level_order_array_to_tree(arr)
    print inorder_iteration(root)
