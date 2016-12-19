def spiralOrder(A):
    ## Actual code to populate result
    top=0
    bottom = len(A)
    right = len(A[0])
    left = 0
    direction = 0
    result = []
    while(top<bottom and left<right):
        if direction == 0:
            for index in xrange(left, right):
                result.append(A[top][index])
            top+=1
        elif direction == 1:
            for index in xrange(top, bottom):
                result.append(A[index][right-1])
            right-=1
        elif direction == 2:
            for index in xrange(right, left, -1):
                result.append(A[bottom-1][index-1])
            bottom-=1
        elif direction == 3:
            for index in xrange(bottom, top, -1):
                result.append(A[index-1][left])
            left+=1
        direction=(direction+1)%4
    return result

print spiralOrder([[1,2],[3,4],[5,6]])
print spiralOrder([[1]])
print spiralOrder([[1,2, 3], [4, 5,6]])
