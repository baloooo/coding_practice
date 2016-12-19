from math import ceil

A = [1, 2, 3, 1, 1]
A = '0 1 0 0 2 0 3'
A = '0 1 0 0 2 0 3 3'
A = [int(x) for x in A.split(' ')]
n = len(A)
candidate1 = candidate2 = 0
balancer1 = balancer2 = 0
for ele in A:
    if ele == candidate1:
        balancer1+=1
    elif ele == candidate2:
        balancer2+=1
    elif balancer1!=0:
        balancer1-=1
    elif balancer2!=0:
        balancer2-=1
    elif balancer1 == 0:
        candidate1 = ele
        balancer1 = 1
    elif balancer2 == 0:
        candidate2 = ele
        balancer2 = 1

balancer1 = balancer2 = 0
for ele in A:
    if ele == candidate1:
        balancer1+=1
    elif ele == candidate2:
        balancer2+=1
threshold = ceil(n/3)
print threshold
print balancer1, balancer2
if balancer1>threshold:
    print candidate1
elif balancer2>threshold:
    print candidate2
else:
    print -1
