# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
	'''
	https://discuss.leetcode.com/topic/28041/recursive-preorder-python-and-c-o-n
    Idea: 
        Serialize:
            Do an preorder on the tree, and while traversal keep adding values of nodes to a shared list
        DeSerialize:
            Iterate over the string to get value of individual nodes and contruct root.left and right recursively from there.
	'''

    def _serialize(self, root, serialized_tree):
        if root is not None:
            serialized_tree.append(str(root.val))
            self._serialize(root.left, serialized_tree)
            self._serialize(root.right, serialized_tree)
        else:
            serialized_tree.append('#')

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_tree = []
        self._serialize(root, serialized_tree)
        return ' '.join(serialized_tree)
        
    def _unserialize(self, serialized_tree):
        val = next(serialized_tree)
        if val == '#':
            return None
        else:
            root = TreeNode(int(val))
            root.left = self._unserialize(serialized_tree)
            root.right = self._unserialize(serialized_tree)
            return root    

    def deserialize(self, serialized_tree):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serialized_tree = iter(serialized_tree.split())
        return self._unserialize(serialized_tree)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
