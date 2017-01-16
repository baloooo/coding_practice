from linkedlistbase import construct_linked_list_from_array, Node, print_linked_list


def merge_k_sorted_lists(list_head):
    original_head = merged_link_list = Node(None)
    while list_head:
        min_ll_head = min(list_head, key=lambda cur_head: cur_head.val)
        merged_link_list.next = min_ll_head
        merged_link_list = merged_link_list.next
        list_head.remove(min_ll_head)
        if min_ll_head.next != None:
            list_head.append(min_ll_head.next)
    return original_head.next

if __name__ == '__main__':
    arr_list = [[10, 15, 25], [5, 12, 20], [1, 4, 7, 11, 17, 22]]
    # arr_list = []
    sorted_list = []
    for arr in arr_list:
        sorted_list.append(construct_linked_list_from_array(arr))
    print_linked_list(merge_k_sorted_lists(sorted_list))
