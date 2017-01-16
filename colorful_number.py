def colorful_number(A):
    num = str(A)
    contiguous_subsequence_set = set()
    num_len = len(num)
    subset_prod_set = set()
    subset_len = 1
    while(subset_len <= num_len):
        i = 0
        while(subset_len+i<=num_len):
            contiguous_subsequence_set.add(num[i:i+subset_len])
            i+=1
        subset_len += 1
    for subset in contiguous_subsequence_set:
        subset_product = 1
        for ele in subset:
            subset_product *= int(ele)
        subset_prod_set.add(subset_product)
    if len(subset_prod_set) == len(contiguous_subsequence_set):
        return 1
    else:
        return 0

if __name__ == '__main__':
    print colorful_number(99)
