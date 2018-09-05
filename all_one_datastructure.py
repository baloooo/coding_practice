'''
Idea is same as LFU:
    Create a doubly LL which is sorted on count for keys
    key_to_count_map contains map of which key has what count, so on increment you can increment/decrement this.
    Also we have count_to_node_map which contains count to set of LL node object mapping.

    On every inc/decr request increase count in key_to_count_map now get the node from count_to_node_map and remove it from there. which should be O(1) in doublyLL.
    Now add this node in count_to_node_map with new count

Implementation : https://leetcode.com/problems/all-oone-data-structure/discuss/91416/Java-AC-all-strict-O(1)-not-average-O(1)-easy-to-read
'''
