n, k = [int(x) for x in raw_input().strip().split(' ')]

arr = [int(x) for x in raw_input().strip().split(' ')]
# max_size = 0
# for x in xrange(len(arr)):
#     final_arr = []
#     final_arr.append(arr[x])
#     temp = arr[x]
#     arr[x] = arr[0]
#     arr[0] = temp
#     for ele in arr[1:]:
#         for each in final_arr:
#             if ((ele+each)%k)==0:
#                 break
#         else:
#             final_arr.append(ele)
# 
#     if len(final_arr)>max_size:
#         max_size = len(final_arr)
# 
# 
# print max_size
final_set = set()
for upper_bound in xrange(n, 0, -1):
    lower_bound = 0
    while(upper_bound+lower_bound<=n):
        final_set_list.append(set(arr[lower_bound:upper_bound]))
        lower_bound+=1
    # for lower_bound in xrange(upper_bound):
    #     if upper_bound+lower_bound>n:
    #         break
    #     final_set_list.append(set(arr[lower_bound:upper_bound]))
print final_set_list

