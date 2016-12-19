def next_permutation(A):
    if not len(A)>2:
        return A
    inflexion_index = -1
    # find inflexion
    for i in xrange(len(A)-1, 1, -1):
        if (A[i]<A[i-1] and A[i-1]>A[i-2]) or (A[i]>A[i-1] and A[i-1]<A[i-2]):
            inflexion_index = i-2
            break 
    else:
        # Totally increasin sequence
        if A[0]>A[1] and A[1]>A[2]:
            return A[::-1]
        # Totally decreasing sequence
        A[-1], A[-2] = A[-2], A[-1]
        return A

    if A[inflexion_index]>A[inflexion_index+1] and A[inflexion_index+1] < A[inflexion_index+2]:
        #increasing suffix
        A[-1], A[-2] = A[-2], A[-1]
        return A 

    # find immediate next to inflexion digit
    min_max = A[inflexion_index]+1
    min_max_index = -1
    print inflexion_index
    for index, ele in enumerate(A[inflexion_index+1:], start=inflexion_index+1):
        if ele > A[inflexion_index] and ele <=min_max:
            min_max_index = index
            break
    else:
        min_max_index = inflexion_index+1

    A[inflexion_index], A[min_max_index] = A[min_max_index], A[inflexion_index]
    A = A[:inflexion_index+1] + A[inflexion_index+1:][::-1]
    return A

if __name__ == '__main__':
    #arr = '444 994 508 72 125 299 181 238 354 223 691 249 838 890 758 675 424 199 201 788 609 582 979 259 901 371 766 759 983 728 220 16 158 822 515 488 846 321 908 469 84 460 961 285 417 142 952 626 916 247 116 975 202 734 128 312 499 274 213 208 472 265 315 335 205 784 708 681 160 448 365 165 190 693 606 226 351 241 526 311 164 98 422 363 103 747 507 669 153 856 701 319 695 52'
    #arr = '626 436 819 100 382 173 817 581 220 95 814 660 397 852 15 532 564 715 179 872 236 790 223 379 83 924 454 846 742 730 689 112 110 516 85 149 228 202 988 212 69 602 887 445 327 527 347 906 54 460 517 376 395 494 827 448 919 799 133 879 709 184 812 514 976 700 156 568 453 267 547 8 951 326 652 772 213 714 706 972 318 768 506 59 854 422'
    arr = '90 80 85 82'
    arr = '35 25 30 20 10'
    inp_arr = [int(x) for x in arr.split(' ')]
    #print next_permutation([101, 42, 891, 991])
    print next_permutation(inp_arr)
