def generate_prefix_arr(needle):
    '''
    Idea: https://www.youtube.com/watch?v=KG44VoDtsAA 
    This array will tell us that for an array ending at this index what is the longest prefix
    that is also the suffix in this 'subarray' ending at this index.
    Therefore when a mismatch occurs b/w needle and haystack we can look up this array to know
    how many indices to move back so as to preseve the matched chars.
    '''
    pre, cur = 0, 1
    pre_arr = [0]*len(needle)
    while cur < len(needle):
        if needle[cur] == needle[pre]:
            '''value of cur is whatever we've matched till now(depicted by pre which is back pointer moving
            along as prefix is equal to suffix)'''
            pre_arr[cur] = pre + 1
            pre += 1
            cur += 1
        else:
            if pre != 0:
                '''we do this b'coz this gives us the index in needle where prev longest
                suffix = prefix resides can be found from pre_arr at index 'pre-1' '''
                pre = pre_arr[pre-1]
            else:
                # But if pre == 0 which means there are no last know prefix=suffix combinations just add zero to pre_arr
                # signalling that no suffix=prefix combinations at this index of needle if mismatch occurs w/ haystack.
                pre_arr[cur] = 0
                cur += 1
    return pre_arr

def strstr(haystack, needle):
    """
    Idea: https://www.youtube.com/watch?v=GTJr8OvyEVQ
    https://stackoverflow.com/documentation/algorithm/7118/substring-search/27462/python-implementation-of-kmp-algorithm#t=201707100128223702031
    """
    # haystack_index: denoting the position within haystack where the prospective match for needle begins
    # needle_index: denoting the index of the currently considered character in needle.
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_arr = generate_prefix_arr(needle)
    haystack_index = needle_index = 0
    while((needle_index<needle_len) and (haystack_index<haystack_len)):
        if haystack[haystack_index] == needle[needle_index]:
            needle_index += 1
            haystack_index += 1
        else:
            if needle_index != 0:
                needle_index = prefix_arr[needle_index-1]
            else:
                haystack_index += 1
    if needle_index==needle_len and haystack[haystack_index-1] == needle[needle_index-1]:
        return haystack_index - needle_len
    else:
        return -1

if __name__ == '__main__':
    # needle = 'acacagt'
    needle = 'abcaby'
    haystack = 'abxabcabcaby'
    haystack = 'ABC ABCDAB ABCDABCDABDE'
    needle = 'ABCDABD'
    print strstr(haystack, needle)
