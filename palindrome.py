import re

regex = re.compile('[^a-zA-Z0-9]')
inp_str = "A man, a plan, a canal: Panama"
inp_str = ''
final_str = regex.sub('', inp_str)
final_str = final_str.lower()
n = len(final_str)
for index in xrange(n):
    if final_str[index] != final_str[-(index+1)]:
        print "not a palindrome"
        break
else:
    print "palindrome"
