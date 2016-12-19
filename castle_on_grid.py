from Queue import Queue

q = Queue()
n = int(raw_input().strip())
inp_arr = []
for i in xrange(n):
    inp_arr.append([[x,0] for x in raw_input().strip()])

start_x, start_y, final_x, final_y = [int(x) for x in raw_input().strip().split(' ')]
total_steps = 0

def bfs(x, y):
    global q
    global total_steps
    if (x == final_x) and (y == final_y):
        print "success"
        x, y = inp_arr[x][y][-1]
        print inp_arr
        while inp_arr[x][y][-1]:
            x, y = inp_arr[x][y][-1]
            print x, y
            raw_input()
            total_steps+=1
        print total_steps
        exit()
    if ((x+1)<n) and (inp_arr[x+1][y][1] != 1) and (inp_arr[x+1][y][0] != 'X'):
        q.put((x+1, y))
    if ((y+1)<n) and (inp_arr[x][y+1][1] != 1) and (inp_arr[x][y+1][0] != 'X'):
        q.put((x, y+1))
    if ((x-1)>=0) and (inp_arr[x-1][y][1] != 1) and (inp_arr[x-1][y][0] != 'X'):
        q.put((x-1, y))
    if ((y-1)>=0) and (inp_arr[x][y-1][1] != 1) and (inp_arr[x][y-1][0] != 'X'):
        q.put((x, y-1))
    if not q.empty():
        new_x, new_y = q.get()
        inp_arr[new_x][new_y][1] = 1
        inp_arr[new_x][new_y].append([x,y])
        bfs(new_x, new_y)

# markin initial node as visited
# Format of node (data, visited_status, prev_node)
inp_arr[start_x][start_y][1] = 1
inp_arr[start_x][start_y].append(None)
bfs(start_x, start_y)
# optionally can print -1 for path not found
