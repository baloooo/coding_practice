inp_arr = [3, 4, 1, 4, 1]
final_set = set()
for ele in inp_arr:
    if ele not in final_set:
        final_set.add(ele)
    else:
        print ele
        # return ele
else:
    print -1
    #return -1
