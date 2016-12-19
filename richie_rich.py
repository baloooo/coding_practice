from sys import exit

n, k = [int(x) for x in raw_input().strip().split(' ')]

num = raw_input().strip()
i=0
j=n-1
# max_num = max(list(num))
max_num = '9'
if n ==1:
    print max_num
    exit()
while i<=j:
    if num[i] != num[j]:
        if k:
            if num[i]>num[j]:
                num = num[:j] + max_num + num[j+1:]
                num = num[:i] + max_num + num[i+1:]
                # num[j] = num[i]
            else:
                num = num[:i] + max_num + num[i+1:]
                num = num[:j] + max_num + num[j+1:]
                # num[i] = num[j]
            k-=1
        else:
            print -1
            break
    i+=1
    j-=1
else:
    if not k and i<=j:
        print -1
    else:
        print num
