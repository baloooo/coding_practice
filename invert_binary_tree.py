from tree_base import level_order_array_to_tree, print_tree_dfs


def invert_tree(root):
    if root == None:
        return
    else:
        root.left, root.right = root.right, root.left
        invert_tree(root.left)
        invert_tree(root.right)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = level_order_array_to_tree(arr)
    print_tree_dfs(root)
    invert_tree(root)
    print 'after inversion'
    print_tree_dfs(root)
