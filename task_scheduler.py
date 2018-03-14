import heapq

class Solution:
    def __init__(self):
        pass

    def my_func(self, tasks, cool_time):
        task_pq = []  # task priority queue.
        cool_down_list = []  # tasks waiting to spend their cool down time.
        tick = 0  # measure of time that has passed.
        task_freq_map = collections.defaultdict(int)  # task -> freq map
        for task in tasks:
            task_freq_map[task] += 1
        for task, freq in task_freq_map.items():
            # Adding -freq b'coz we want max heap and not min heap.
            task_pq.append([task, -freq, 0]) # Task name, freq, cool time
	# If there're pending tasks in priority q or waiting in cool down list keep running CPU(tick).
        while len(task_pq) != 0 or len(cool_down_list) != 0:
            tick += 1
            heapq.heapify(task_pq)
            cur_task = None
	    if len(task_pq): # If there's atleast one process in current task_q
                cur_task = heapq.heappop(task_pq)
                cur_task[1] += 1
            temp = []
            # Decrease cool down time for all waiting tasks.
            for task in cool_down_list:
                task[2] -= 1
                if task[2] == 0:
                    heapq.heappush(task_pq, task)
                else:
                    temp.append(task)
            cool_down_list = temp
            if cur_task and cur_task[1] != 0:
                if cool_time == 0:
                    heapq.heappush(task_pq, cur_task)
                else:
                    cur_task[2] = cool_time # set cur task to wait for cool_time in cool_down list.
                    cool_down_list.append(cur_task)
        return tick 

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
