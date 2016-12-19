count = 1 
def permute(list_string, start, end):
    global count
    string_set = set()
    if start==end:
        print count
        print ''.join(list_string)
        count+=1
    else:
        for i in xrange(start, end+1):
            if list_string[i] in string_set:
                continue
            list_string[start], list_string[i] = list_string[i], list_string[start]
            permute(list_string, start+1, end)
            list_string[start], list_string[i] = list_string[i], list_string[start]
            string_set.add(list_string[i])

if __name__ == '__main__':
    string = 'aabc'
    n = len(string)
    list_string = list(string)
    permute(list_string, 0, n-1)
