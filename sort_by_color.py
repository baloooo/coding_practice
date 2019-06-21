class Solution(object):
    def sortColors(self, arr):
        """
        http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
        Variant with 4 colors:

        https://stackoverflow.com/a/3436595/2795050
        RRRRBBB???????????YYYYGGGG
               ^
        B: ignore
        R: replace with first B
        Y: while replace with first Y
        G:
            replace cur with last Y
            replace Y with first Y
            perform while
        """
        lo, mid, hi = 0, 0, len(arr)-1
        while mid <= hi: # Note: equal sign, since hi sits on an unknown value mid should go up until hi.
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo += 1
                mid += 1
                '''since lo rests on a 1 and not 0 the swap gives mid pos'n a 1
                therefore mid also needs to move forward'''
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi -= 1
                #Note: since mid and hi are both at unknown pos'n hi-=1 brings it again to unknown
                # and since mid was now swapped with an unknown from hi it can continue from there.