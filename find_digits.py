n = int(raw_input().strip())

for i in xrange(n):
    digit = int(raw_input().strip())
    str_digit = str(digit)
    evenly_div_digits = 0
    for each in str_digit:
        if int(each) and digit%int(each) == 0:
            evenly_div_digits+=1
    print evenly_div_digits
    
