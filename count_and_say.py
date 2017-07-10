

class Solution:

    def count_and_say(self, n):
        arr = [1]
        for _ in xrange(n-1):
            res = []
            cur_ele, cur_count = arr[0], 1
            for i in xrange(1, len(arr)):
                if arr[i] != cur_ele:
                    res.append(cur_count)
                    res.append(cur_ele)
                    cur_ele = arr[i]
                    cur_count = 1
                else:
                    cur_count += 1
            res.append(cur_count)
            res.append(cur_ele)
            arr = res
        return ''.join([str(x) for x in arr])

if __name__ == '__main__':
    test_cases = [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
    ]
    for test_case in test_cases:
        res = Solution().count_and_say(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
