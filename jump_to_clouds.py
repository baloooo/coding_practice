n = int(raw_input().strip())
jumps = 0
arr = [int(x) for x in raw_input().strip().split(' ')]
i=0
while(i<n):
    if i+2<n-1:
        if arr[i+2] != 0:
            i+=1
        else:
            i+=2
        jumps+=1
    else:
        jumps+=1
        break

print jumps



