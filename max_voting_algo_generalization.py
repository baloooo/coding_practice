# return (any one) integer that repeats more than n/k times, k being 3 in this case

from math import ceil

inp_arr = '1 2 3 1 1'
inp_arr = '1000662 1000975 1000662 1000306 1000662 1000488 1000662 1000732 1000397 1000769 1000662 1000731 1000454'
A = [int(x) for x in inp_arr.split(' ')]
n = len(A)

cand1 = cand2 = count1 = count2 = 0
for ele in A:
    if ele == cand1:
        count1+=1
    elif ele == cand2:
        count2+=1
    elif count1 == 0:
        cand1 = ele
        count1+=1
    elif count2 == 0:
        cand2 = ele
        count2+=1
    else:
        count1-=1
        count2-=1

count1 = count2 = 0

for ele in A:
    if ele == cand1:
        count1+=1
    elif ele == cand2:
        count2+=1
print cand1, count1, cand2, count2
if count1>count2 and count1>=ceil(n/3.0):
    print cand1
elif count2>ceil(n/3.0):
    print cand2
else:
    print -1
