n = int(raw_input().strip())
arr = [int(x) for x in raw_input().strip().split(' ')]
backup_arr = []
# def smallest(arr):
#     min_arr = arr[0]
#     for ele in arr:
#         if ele<min_arr:
#             min_arr = ele
#     return min_arr            

while arr:
    min_arr = min(arr)
    print len(arr)
    for ele in arr:
        if ele-min_arr<=0:
            continue
        backup_arr.append(ele-min_arr)
    arr = backup_arr
    backup_arr = []
