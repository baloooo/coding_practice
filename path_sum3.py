# Defintion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
	Idea: https://discuss.leetcode.com/topic/65100/python-solution-with-detailed-explanation
	Brute Force Solution

	The simplest solution is to traverse each node (preorder traversal) and then find all paths
	which sum to the target using this node as root.
	The worst case complexity for this method is N^2.
	If we have a balanced tree, we have the recurrence: T(N) = N + 2T(N/2).
	This is the merge sort recurrence and suggests NlgN. Notice contrary to merge sort where we
	make sure list is divided in two two halves(arbitrarly) here if there is no root.left we can
	easily get a one sided linear list type tree which would be then somewhat equal to quicksort
	worst case and therefore O(n^2)
	Imagine a balanced tree and think about it this way:

How many nodes do I need to scan to find all sums which start from the root? Answer: N

How many nodes do I need to scan to find all sums which start from root.left? Answer: N/2

How many nodes do I need to scan to find all sums which start from root.right? Answer: N/2

For the first and second level, we have N + 2(N/2) or 2*N scans. How many total levels do we have in a balanced tree ? Answer lgN. Therefore for a balanced tree it takes N * lg(N)

Imagine a linear list for the worst case

Using the first node as root, we scan N items

Using the second node as root, we scan N-1 items

For all nodes as potential roots or start points, we have: N + (N-1) + (N-2) +... = N^2
    '''
    def find_sum(self, root, target_sum):
        # find target_sum with this root as the root of the sub-tree
        if root:
            # since values can be negative or zero, this will ensure we add 1 every time we hit our target_sum
            return (
                int(target_sum == root.val) +
                self.find_sum(root.left, target_sum-root.val) +
                self.find_sum(root.right, target_sum-root.val))
        else:
            return 0
        
    def pathSum_bruteforce(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return (
                self.find_sum(root, target_sum) +
                self.pathSum_bruteforce(root.left, target_sum) +
                self.pathSum_bruteforce(root.right, target_sum))
        else:
            return 0

#################################################################################################################

    def find_sum(self, root, target_sum, sum_until_now, prefix_sum):
        '''
        diagram: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-:-)
        '''
        if not root: return
        sum_until_now = sum_until_now + root.val
        complement_sum = sum_until_now - target_sum
        if complement_sum in prefix_sum:
            self.paths += prefix_sum[complement_sum]
        prefix_sum[sum_until_now] += 1
        self.find_sum(root.left, target_sum, sum_until_now, prefix_sum)
        self.find_sum(root.right, target_sum, sum_until_now, prefix_sum)
        prefix_sum[sum_until_now] -= 1
            

    def pathSum_optimized(self, root, target_sum):
        """
        Time:
        Idea: Idea is to have a running sum of nodes(or arr values) and at each step check
        if (target-running_sum) is already in prefix_sum_to_count map.
        Notice this idea can be easily extended to find a subarray with target sum which would
        generally be O(n^2) but with this hash_map strategy would be O(n) time and O(n) space.
        Idea: https://discuss.leetcode.com/topic/65100/python-solution-with-detailed-explanation/10
        """
        if not root: return 0
        self.paths = 0
        # {prefix_sum untill this node: number of paths that have the same sum}
        prefix_sum = collections.defaultdict(int)
        sum_until_now = 0
        # Note: Adding this is very crucial, since when you start from a sub-tree,
        prefix_sum[0] = 1
        self.find_sum(root, target_sum, sum_until_now, prefix_sum)
        return self.paths
