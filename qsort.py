from time import sleep

def partition(arr, lo, hi):
    pivot = arr[hi]
    base = lo - 1
    while(lo<hi):
        if arr[lo]<pivot:
            base+=1
            arr[base], arr[lo] = arr[lo], arr[base]
        lo+=1
    arr[base+1], arr[hi] = arr[hi], arr[base+1]
    return base+1

def qsort(arr, lo, hi):
    if lo<hi:
        part = partition(arr, lo, hi)
        qsort(arr, lo, part-1)
        qsort(arr, part+1, hi)

if __name__ == '__main__':
    arr = [50, 40, 10, 20, 60, 30]
    arr = [50, 40, 30, 20, 10]
    arr = [20, 10]
    n = len(arr)
    print arr
    qsort(arr, 0, n-1)
    print arr
