"""
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
"""
def sqrt_optimized(self, x):
    if x == 0:
	return 0
    low = 1
    high = x
    while low+1 < high:
	mid = low + (high-low)/2
	if mid*mid > x:
	    high=mid
	else:
	    low=mid
    return low

def sqrt(x):
    # 
    low = 1
    high = x
    if x == 0:
        return 0
    while(1):
        mid = (low+high)/2
        if low+1 == high:
            return low
        square = mid*mid
        if square == x:
            return mid
        if square > x:
            high = mid
            continue
        else:
            low = mid
            continue

if __name__ == '__main__':
    num = 9
    # num = 50
    # num = 4
    # num = 2
    print sqrt(num)
