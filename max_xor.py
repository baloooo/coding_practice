import collections

class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}

class Trie(object):
    def __init__(self, max_len=32):
        self.root = TrieNode('dummy')
        self.binary_format = ''.join(['0', str(max_len), 'b'])

    def add(self, num):
        cur_num = format(num, self.binary_format)
        # add this binary represn of cur_num in trie
        root = self.root
        for digit in cur_num:
            if root.children.get(digit):
                root = root.children[digit]
            else:
                new_node = TrieNode(digit)
                root.children[digit] = new_node
                root = new_node

    def get_max_xor(self, for_num):
        for_num_binary = format(for_num, self.binary_format)
        cur_max_xor = ['0']*len(for_num_binary)
        root = self.root

        for idx, digit in enumerate(for_num_binary):
            complimentary_digit = '1' if digit == '0' else '0'
            if root.children.get(complimentary_digit):
                cur_max_xor[idx] = '1'
                root = root.children[complimentary_digit]
            else:
                root = root.children[digit]
        return int(''.join(cur_max_xor), 2)


class Solution(object):
    def findMaximumXOR_optimized(self, nums):
        '''
        Time: O(n)
        Space: O(n)
        Idea is that it would be great if we could iterate over nums and for each num we can
        scan over all nums to find which num can give the maximum xor with cur num.
        Now to do that for each num at any given index position we need to find prefix of all nums up
        untill that index and see which num from the nums can give us a complimentary bit to the one in
        cur_num.
        Now since trie is the best data structure to process prefixes, we'll use trie to store binary
        representation of all nums.
        And then for cur_num in nums try to glide over trie with complimentary bit positions than our cur_num.
        by the end of the scan for cur_num we'll get a max_xor for cur_num, which is the maximum xor we can
        get for this cur_num with any num in nums.
        We'll do this for all the num in nums and return the max of all.

        Summary:
            Build a Trie with the nodes as 0 and 1. The trie will have the binary representation(32 bit) for each word.
            Traverse down the Trie for each num and calculate the XOR for each.
            Get the maximum.
        binay representation of a num can be got like this:
        In [17]: bin(513)
        Out[17]: '0b1000000001'

        In [18]: bin(0)
        Out[18]: '0b0'

        In [19]: bin(-1)
        Out[19]: '-0b1'
        Notice that bin method automatically gives the min no. of digits to represent a num, also
        the negative sign is shown separately and not on MSB as would be in 2's complement method.
        or one can use the format method:
            format(num, 010b), where second param is padding_digit(0) + total_representation_len(10), encoding(b)
        '''

        # only store bits up to the bits used in max_num
        max_len = len(bin(max(nums)))-2 # -2 b'coz leading 0b are to be neglected.
        trie = Trie(max_len)
        for num in nums:
            trie.add(num)
        max_xor_sofar = 0
        for cur_num in nums:
            max_xor_for_cur_num = trie.get_max_xor(cur_num)
            max_xor_sofar =  max(max_xor_sofar, max_xor_for_cur_num)

        return max_xor_sofar

    def findMaximumXOR(self, nums):
        """
        http://www.leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91049/Java-O(n)-solution-using-bit-manipulation-and-HashMap/95535
        """
        max_xor = 0
        mask = 0
        for i in xrange(31, -1, -1):
            # The mask will grow like  100..000 , 110..000, 111..000,  then 1111...111
            # for each iteration, we only care about the left parts
            mask = mask | (1<<i)
            # we only care about the left parts, for example, if i = 2, then we have
            #   {1100, 1000, 0100, 0000} from {1110, 1011, 0111, 0010}*/
            interested_bits_nums_set = {num & mask for num in nums}
            next_max_xor = max_xor | (1 << i)
            """
            This is the most tricky part, coming from a fact that if a ^ b = c, then a ^ c = b;
            now we have the 'c', which is greedyTry, and we have the 'a', which is leftPartOfNum
            If we hope the formula a ^ b = c to be valid, then we need the b, 
            and to get b, we need a ^ c, if a ^ c exisited in our set, then we're good to go
            """
            for num in interested_bits_nums_set:
                if (next_max_xor ^ num) in interested_bits_nums_set:
                    max_xor = next_max_xor
                    break
        return max_xor

if __name__ == '__main__':
    test_cases = [
        ([3, 10, 5, 25, 2, 8], 28),
    ]
    for test_case in test_cases:
        res = Solution().findMaximumXOR_optimized(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
