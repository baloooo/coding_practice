from itertools import combinations, chain


def get_power_set_list_comprehension(arr):
    power_set = [[]]
    """
    # for every additional element in our set
      the power set consists of the subsets that don't
      contain this element (just take the previous power set)
      plus the subsets that do contain the element (use list
      comprehension to add [x] onto everything in the
      previous power set.
    O/P: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    for ele in arr:
        power_set.extend([subset + [ele] for subset in power_set])
    return power_set


def get_power_set_iter_tools(arr):
    arr_len = len(arr)
    power_set = []
    for subset in chain.from_iterable([combinations(arr, set_size) for set_size in xrange(1, arr_len+2)]):
        power_set.append(subset)
    return power_set

if __name__ == '__main__':
    arr = [1, 2, 3]
    print get_power_set_list_comprehension(arr)
    print get_power_set_iter_tools(arr)
