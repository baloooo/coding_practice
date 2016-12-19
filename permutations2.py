def permute(list_string, start, end):
    if start==end:
        print "".join(list_string)
    else:
        for i in xrange(start, end+1):
            list_string[i], list_string[start] = list_string[start], list_string[i]
            permute(list_string, start+1, end)
            list_string[start], list_string[i] = list_string[i], list_string[start]

if __name__ == '__main__':
    string = 'abc'
    list_string = list(string)
    permute(list_string, 0, 2)
