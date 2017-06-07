"""
1211
"""
n = 1
for _ in xrange(n):
    input_seq = '3 1 2 1 1'  # raw_input().strip.split(' ')
    item_count, cur_index = 0, 0
    inp_char, char_count = input_seq[cur_index], 1
    while cur_index < len(input_seq):
        inp_char, char_count = input_seq[cur_index], 1
        for count in xrange(char_count, len(input_seq)):
            if input_seq[count] != inp_char:
                break
            print '.',
            char_count += 1
        print char_count, inp_char
        item_count += 2
        cur_index += 1
    print item_count
