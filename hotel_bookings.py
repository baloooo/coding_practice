arrive = [int(x) for x in raw_input().strip().split(' ')]
depart = [int(x) for x in raw_input().strip().split(' ')]
k=int(raw_input().strip())
book=0
i=j=0
arrive.sort()
depart.sort()
while(i<len(arrive)):
    if arrive[i]<depart[j]:
        book+=1
        if book>k:
            print False
            exit()
        i+=1
    else:
        book-=1
        j+=1

print True

