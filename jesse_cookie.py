from Queue import PriorityQueue

# n, limit = map(int, raw_input().strip().split(' '))
n = 621775
limit = 401226849
q = PriorityQueue()
with open("tc4.txt") as test_cases:
    for test_case in test_cases:
        # for each in raw_input().strip().split(' '):
        for each in test_case.split(' '):
            q.put(int(each))

count = 0 
if not q.empty():
    x=q.get()
    while(x<limit):
        if q.empty():
            print "q empty", -1
            break
        cookie = x + 2*q.get()
        q.put(cookie)
        if q.empty():
            break
        count+=1
        x=q.get()
    else:
        print count
else:
    print "empty Q", -1
