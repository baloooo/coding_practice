import Queue

class Solution:
    def __init__(self):
        pass

    def indexes(self, target_ele):
        return [index for cur_ele in arr if cur_ele == target_ele and cur_ele != index]

    def traversal(self, arr):
        n = len(arr)
        result_map = defaultdict(int)
        for i in xrange(n):
            result_map[i]
        result_map[0] = 1
        for index, ele in enumerate(arr):
            if index == ele:
                root = ele
                break
        q = Queue.Queue()
        for ele in indexes(root):
            q.put(ele,1)
        while q:
            cur_ele, cur_distance = q.get()
            adjacent = self.indexes(cur_ele)


            
            

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
