import heapq
import collections

class Task(object):
    def __init__(self, task_id, freq, cool_down_timer):
        self.task_id = task_id
        self.freq = freq
        self.cool_down_timer = cool_down_timer

    def __lt__(self, other):
        if self.freq > other.freq:
            return True

class Solution:
    def __init__(self):
        pass

    def task_scheduler(self, tasks, cool_time):
        '''
        https://leetcode.com/problems/task-scheduler/solution/
        The current code is returning TLE on LC but runs with 160ms in playground, not sure what to do
        since complete test case is also not available.
        '''
        task_pq = []  # task priority queue.
        cool_down_list = []  # tasks waiting to spend their cool down time.
        tick = 0  # measure of time that has passed.
        task_freq_map = collections.defaultdict(int)  # task -> freq map
        for task in tasks:
            task_freq_map[task] += 1
        for task, freq in task_freq_map.items():
            # Adding -freq b'coz we want max heap and not min heap.
            task_pq.append(Task(task, freq, 0)) # Task name, freq, cool time
        # If there're pending tasks in priority q or waiting in cool down list keep running CPU(tick).
        while len(task_pq) != 0 or len(cool_down_list) != 0:
            tick += 1
            heapq.heapify(task_pq)
            cur_task = None
            if len(task_pq) != 0: # If there's atleast one process in current task_q
                cur_task = heapq.heappop(task_pq)
                cur_task.freq -= 1
            temp = []
            # Decrease cool down time for all waiting tasks.
            for task in cool_down_list:
                task.cool_down_timer -= 1
                if task.cool_down_timer == 0:
                    heapq.heappush(task_pq, task)
                else:
                    temp.append(task)
            cool_down_list = temp
            if cur_task and cur_task.freq != 0:
                if cool_time == 0:
                    heapq.heappush(task_pq, cur_task)
                else:
                    cur_task.cool_down_timer = cool_time # set cur task to wait for cool_time in cool_down list.
                    cool_down_list.append(cur_task)
        return tick 

if __name__ == '__main__':
    test_cases = [
        ((["A","A","A","B","B","B"], 2), 8),
    ]
    for test_case in test_cases:
        res = Solution().task_scheduler(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
