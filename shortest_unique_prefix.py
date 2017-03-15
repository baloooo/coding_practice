"""
Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible. 
"""


class Node:
    def __init__(self):
        self.children = {}

    def __repr__(self):
        return 'children {0}'.format(self.children)

class Solution:
    def find_shortest_unique_prefix(self, root, ele):
        prefix = []
        for char in ele:
            if root.children[char][1] == 1:
                prefix.append(char)
                break
            else:
                root = root.children[char][0]
            prefix.append(char)
        return ''.join(prefix)

    def create_trie(self, inp):
        orig_root = root = None
        for ele in inp:
            for char in ele:
                if root is None:
                    orig_root = root = Node()
                try:
                    root.children[char][1] += 1
                except KeyError:
                    root.children[char] = [Node(), 1]
                root = root.children[char][0]
            root = orig_root
        return orig_root

    def shortest_unique_prefix(self, inp):
        # create trie for input
        prefixes = []
        root = self.create_trie(inp)
        import ipdb; ipdb.set_trace()
        for ele in inp:
            prefixes.append(self.find_shortest_unique_prefix(root, ele))
        return prefixes


if __name__ == '__main__':
    inp = ["zebra", "dog", "duck", "dove"]
    print Solution().shortest_unique_prefix(inp)
