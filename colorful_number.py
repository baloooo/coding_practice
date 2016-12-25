def colorful_number(A):
    from itertools import combinations, chain
    arr = [int(x) for x in str(A)]
    power_set = []
    arr_len = len(arr)
    subset_prod_set = set()
    for subset in chain.from_iterable(combinations(arr, set_len) for set_len in xrange(1, arr_len+2)):
        power_set.append(subset)
    for subset in power_set:
        subset_product = 1
        for ele in subset:
            subset_product *= ele
        subset_prod_set.add(subset_product)
    print subset_prod_set
    if len(subset_prod_set) == ((2**arr_len) -1):
        return 1
    else:
        return 0

if __name__ == '__main__':
    print colorful_number(263)
