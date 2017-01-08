def merge(arr, lo, mid, hi):
    m = mid-lo+1
    n = hi-mid
    LO = [0]*m
    HI = [0]*n
    # copy arr to LO and HI
    for i in xrange(m):
        LO[i] = arr[lo+i]
    for j in xrange(n):
        HI[j] = arr[mid+1+j]
    i = j = 0
    k = lo
    while(i<m and j<n):
        if LO[i]<HI[j]:
            arr[k] = LO[i]
            i+=1
        else:
            arr[k] = HI[j]
            j+=1
        k+=1
    if i<m:
        arr[k:hi+1] = LO[i:]
    if j<n:
        arr[k:hi+1] = HI[j:]

def msort(arr, lo, hi):
    if lo<hi:
        mid = lo + (hi - lo)/2
        msort(arr, lo ,mid)
        msort(arr, mid+1, hi)
        merge(arr, lo, mid, hi)

if __name__ == '__main__':
    arr = [2, 10, 1, 6, 5]
    print 'orginal array: ', arr
    n = len(arr)
    msort(arr, 0, n-1)
    print 'final arr: ', arr
