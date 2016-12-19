freq_list = [int(x) for x in raw_input().strip().split(' ')]

string = ''
for index, freq in enumerate(freq_list, start=0):
    string += chr(97+index)*freq

def calculate_border(string):
    border=0
    for index in xrange(len(string)):
        if string[:index] == string[-index]:
            border+=1


print string
string_border = calculate_border(string)

# for each_string in permutation(string):
#    sum_border = calculate_border(each_string)
    
