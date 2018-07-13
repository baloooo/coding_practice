class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
		Idea is to iterate over array and for each element see if there couple is sitting beside them or not.
		If not find where the couple is currently and swap the honorable person sitting beside you with your couple.
		pos_arr keeps the indexes of all elements in row. One can think of pos_arr as its indexes being the values in row array
		and vice-versa. But in essence it's just an array to store positions of elements in the array, so that when we need to
		find our couple in case they are not beside us, we can look up their current position quickly.
		pos_arr (can use dict here too) allows to make the query in O(1) which could have taken us O(n).
        """
        if len(row) < 2: return 0
        swaps = 0
        pos_arr = [0 for _ in xrange(len(row))]
        # arr[i] has the position of i in the row array.
        for idx, ele in enumerate(row):
            pos_arr[ele] = idx

        for idx in xrange(0, len(row), 2):
            me = row[idx]
            my_couple = me - 1 if (me & 1) else me + 1
            if row[idx+1] != my_couple:
                # bring in my couple.
                pos_to_update = row[idx+1] # This is the person who is currently sitting by my side.
                val_to_update_with = pos_arr[my_couple] # This is the place where he will be moved to(where my couple currently is)
                row[idx+1], row[pos_arr[my_couple]] = row[pos_arr[my_couple]], row[idx+1]
                pos_arr[pos_to_update] = val_to_update_with # update position of the person previously sitting by my side in position array, we need not care about correct position in pos_arr for my couple(as that also changed in the swap) b'coz we won't refer that anymore moving forward.
                
                swaps += 1
        return swaps
