'''
Implementaion is very close to LFU.
Code and idea: https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments
Diagram helps it best:
key_to_freq_map helps to find a freq for the key you want to do operation on.

The doubly linkedlist maintains the sorted order of frequencies

freq_to_node_map gives a node for each freq.
    This node will have all list of keys(words) with the same frequency
    When you increment/decrement/delete move this key over to next/prev freq_node

'''
