import string

n = int(raw_input().strip())
rocks = set(string.ascii_lowercase)
for i in xrange(n):
    rocks &= set(raw_input().strip())
print len(rocks)
