n = int(raw_input().strip())
for i in xrange(n):
    tc_len = int(raw_input().strip())
    inp_queue = [int(x) for x in raw_input().strip().split(' ')]
    swaps = 0
    # check for Too chaotic
    for index, ele in reversed(list(enumerate(inp_queue, start=1))):
        if ele-index>2:
            print "Too chaotic"
            break
    else:
        for i in xrange(tc_len):
            for j in xrange(i, 0, -1):
                if inp_queue[j] < inp_queue[j-1]:
                    temp = inp_queue[j]
                    inp_queue[j] = inp_queue[j-1]
                    inp_queue[j-1] = temp
                    swaps+=1
                else:
                    break
        print swaps



