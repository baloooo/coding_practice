from Queue import Queue

area = []
q = Queue()
n = int(raw_input().strip())
for i in xrange(n):
    p, d = map(int, raw_input().strip().split(' '))
    if p>d:
        q.put([p, d])
    area.append([p, d])

while not q.empty():
    petrol, distance = q.get()
    index = area.index([p,d])
    i = index + 1
    while(i!=index):
        new_petrol, new_distance = area[i]
        total_petrol = petrol - distance + new_petrol
        if total_petrol < new_distance:
            break
        petrol = total_petrol
        distance = new_distance
        i = (i+1) % len(area)
    else:
        print index
        break
