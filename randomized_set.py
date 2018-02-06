'''
https://discuss.leetcode.com/topic/53234/2-python-implementations-using-dictionary-and-list-syned-and-asyned-with-explanation/5
'''

import random
import collections

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.vals_to_index = {} # value to index in vals array.
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.vals_to_index:
            return False
        else:
            # Notice that length is pushed in not len-1 since we're adding the element afterwards
            self.vals_to_index[val] = len(self.vals)
            self.vals.append(val)
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        
        Removal strategy is similar to removal of element from a min heap.
        Replace the element to be removed with the last element of the tree.
        Adjust the last element in accordance with the min heap property
        Remove the last element"""
        if val not in self.vals_to_index:
            return False
        cur_val_index, last_ele = self.vals_to_index[val], self.vals[-1]
        self.vals[cur_val_index], self.vals_to_index[last_ele] = last_ele, cur_val_index
        del self.vals_to_index[val]
        self.vals.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
Extension of the above can be when duplicates are allowed for the vals that are inserted and we would want to keep
all duplicated values as well and remove them one by one. Also while giving back random from the vals take in account
the repetition.
'''

class RandomizedCollection(object):

    def __init__(self):
        """
        https://discuss.leetcode.com/topic/53896/frugal-python-code
        Initialize your data structure here.
        """
        self.vals, self.vals_to_index = [], collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.vals_to_index[val].add(len(self.vals)) # Notice that length is pushed in not len-1 since we're adding the element afterwards
        self.vals.append(val)
        return len(self.vals_to_index[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        Get any index from the set of locations in vals_to_index, and replace that location with end element as in the regular case.
        """
        # if val not in self.vals_to_index:
        # 	return False
		# Can't do above since we're not explicitly deleting keys from defaultdict so the only way to check is
		# if set on the key is empty.
        if self.vals_to_index[val]:
            cur_val_index, last_ele = self.vals_to_index[val].pop(), self.vals[-1]
            self.vals[cur_val_index] = last_ele
            # Note: Add to the set before you remove else can get a IndexError, testcase in link above
            self.vals_to_index[last_ele].add(cur_val_index)
            self.vals_to_index[last_ele].discard(len(self.vals)-1)
            self.vals.pop()
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vals)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == '__main__':
    #test_case = (["insert","insert","insert","insert","insert","remove","remove","remove","remove"],
	#			[[4],[3],[4],[2],[4],[4],[3],[4],[4]])
    #test_case = (["insert","insert","insert","insert","insert","insert","insert","insert","insert","remove","remove"],
    #             [[1],[0],[1],[1],[1],[1],[1],[1],[0],[0],[0]])
    test_case = (["insert","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom",
                  "getRandom","getRandom","getRandom","getRandom","getRandom"],
                 [[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]])
    sol_obj = RandomizedCollection()
    for method, arg in zip(*test_case):
        print getattr(sol_obj, method)(*arg)
