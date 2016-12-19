# TODO: check for heap based on arbitrary tuple element
from heapq import heappush, heappop

process_queue = []
input_queue = []
current_time = total_waiting_time = 0
n = int(raw_input().strip())

for _ in xrange(n):
    task_arrival, cpu_time = [int(x) for x in raw_input().strip().split(' ')]
    heappush(input_queue, (task_arrival, cpu_time))

task_arrival, cpu_time = heappop(input_queue)
current_time = task_arrival
#heappush(process_queue, (cpu_time, task_arrival))

current_time += cpu_time
total_waiting_time += current_time - task_arrival


for _ in xrange(n-1):
    task_arrival, cpu_time = heappop(input_queue)
    if task_arrival <= current_time:
        heappush(process_queue, (cpu_time, task_arrival))
        continue
    if len(process_queue):
        processing_task_cpu_time, processing_task_arrival  = heappop(process_queue)
        current_time += processing_task_cpu_time
        total_waiting_time += current_time - processing_task_arrival

    # push outstanding process
    heappush(process_queue, (cpu_time, task_arrival))

while len(process_queue):
    cpu_time, task_arrival  = heappop(process_queue)
    current_time = current_time + cpu_time
    total_waiting_time += current_time - task_arrival

print total_waiting_time/n

