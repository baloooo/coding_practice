def seive(A):
    prime_numbers = []
    num_range = [i for i in xrange(2,A+1)]
    for cur_num in num_range:
	if cur_num!=-1:
	    prime_numbers.append(cur_num)
	    i=2
	    while(cur_num*i<=A):
		num_range[cur_num*i-2]=-1
		i+=1
    return prime_numbers

if __name__ == '__main__':
    print seive(10)
