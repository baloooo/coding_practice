num_array = [1,2,3]
num_array = [1,2,3]
num_array = [0]
num = 0
n = len(num_array)
for i in xrange(n-1, -1, -1):
    num = num+num_array[n-1-i]*pow(10, i)
print num
