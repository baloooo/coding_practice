"""
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
"""


def subset_duplicate_allowed(arr):
    """
    Not complete
    [1, 4] and [4, 1] are same subset but current solution sees them as different
    """
    res = [[]]
    uniq_set = set()
    for ele in arr:
        subsets = [each+[ele] for each in res]
        for subset in subsets:
            subset_tuple = tuple(subset)
            if subset_tuple not in uniq_set:
                uniq_set.add(subset_tuple)
                res.append(subset)
    res.sort()
    return res


def subset_without_duplicates(arr):
    res = [[]]
    for ele in arr:
        res = res + [each+[ele] for each in res]
    return res


if __name__ == "__main__":
    # inp_arr = [1, 2, 3]
    # inp_arr = [1]
    # inp_arr = []
    # inp_arr = [1, 2, 3, 4]
    # inp_arr = [1, 1, 2]
    # inp_arr = [1, 1]
    # inp_arr = [3, 2, 1]
    # inp_arr = [3, 2, 2, 1]
    # inp_arr = [4, 4, 3, 2]
    # inp_arr = [4, 3, 2, 1, 1]
    # print subset_without_duplicates(inp_arr)
    # print subset_duplicate_allowed(inp_arr)
    inp_arr = [4, 4, 4, 1, 4]
    print temp_subset(inp_arr)
