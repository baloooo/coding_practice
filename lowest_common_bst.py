from tree_base import level_order_array_to_tree


def lowest_common_bst_optimized(root, val1, val2):
    # Time: O(n) Space: O(1)
    pass


class Solution:
    def __init__(self):
        self.path = set()

    def lowest_common_bst_naive(self, root, val1, val2):
        # Time: O(2*n) Space: O(n)
        self.dft_add(root, val1)
        return self.dft_find(root, val2)

    # def dft(root, val, search_val2=True):
    #     if root is None:
    #         return
    #     if not search_val2:
    #         root.path.add(root)
    #     else:
    #         if root.val in self.path:
    #             return root
    #     if dft(root.left, val, search_val2):
    #         return root
    #     if dft(root.right, val, search_val2):
    #         if not search_val2:
    #             root.path.remove(root)

    def dft_add(self, root, val):
        if root is None:
            return
        self.path.add(root.val)
        target = self.dft_add(root.left, val)
        if target:
            return target
        target = self.dft_add(root.right, val)
        if target:
            return target
        self.path.remove(root.val)

    def dft_find(self, root, val):
        if root is None:
            return
        if root.val in self.path:
            return root.val
        target = self.dft_find(root.left, val)
        if target:
            return target
        target = self.dft_find(root.right, val)
        if target:
            return target

if __name__ == '__main__':
    arr = [3, 6, 8, 2, 11, None, 13, None, None, 9, 5, 7, None]
    val1, val2, ans = 2, 5, 6
    root = level_order_array_to_tree(arr)
    res = Solution().lowest_common_bst_naive(root, val1, val2)
    print res
    if res == ans:
        print "passed"
    else:
        print "failed"
