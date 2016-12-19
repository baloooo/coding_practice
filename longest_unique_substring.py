"""Using sliding window technique
Test cases
# inp_str = 'GEEKSFORGEEKS'
# inp_str = 'ABDEFGABEF'
# inp_str = 'ABACDE'
# inp_str = 'BBBB'
# inp_str = 'ABCDEF'
# inp_str = 'ABCDAB'
# inp_str = 'ABDEFGABEF'
"""
inp_str = 'BBBB'
inp_set = set()
start_ptr = end_ptr = 0
max_len=0
max_len_start = max_len_end = 0
for char in inp_str:
    if char in inp_set:
        if end_ptr-start_ptr>max_len:
            max_len = end_ptr-start_ptr
            max_len_start = start_ptr
            max_len_end = end_ptr
        for i in xrange(start_ptr, end_ptr):
            if inp_str[i] == char:
                start_ptr = i+1
                end_ptr+=1
                break
            inp_set.remove(inp_str[i])
    else:
        end_ptr+=1
        inp_set.add(char)
if end_ptr-start_ptr>max_len:
    max_len=end_ptr-start_ptr
    max_len_start = start_ptr
    max_len_end = end_ptr
print "maximum length unique substring is %s with length %s" % (inp_str[max_len_start:max_len_end], max_len)
