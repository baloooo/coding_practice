from heapq import heappush, heappop
from Queue import Queue

n = int(raw_input().strip())
heap = []
input_arr = Queue()
# start working on first element
_, current_bust_time = [int(x) for x in raw_input().strip().split(' ')]
total_waiting_time = 0
current_time = 0
start_time = 0

for _ in xrange(n):
    input_arr.put(task_arrival, task_cputime) = [int(x) for x in
        raw_input().strip().split(' ')])

# process_arr = sorted(input_arr, key = lamda process: prcess[0])
for process in process_arr:
    if process[0]<current_burst_time:
        heappush(heap, process)
    else:
        # add waiting time for process
        current_burst_time = heap[0]
        heapify(heap)
        total_waiting_time+=current_burst_time

for _ in xrange(start_time, current_burst_time):
    task_arrival, task_cputime = [int(x) for x in raw_input().strip().split(' ')]
    heappush(heap, (task_arrival, task_cputime))
