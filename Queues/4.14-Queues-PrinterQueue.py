from queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.print_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def get_time_remaining(self):
        return (self.current_task.num_pages / self.print_rate) * 60

    def is_busy(self):
        return self.current_task is not None

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.current_task = None
    
    def start_next_task(self, task):
        self.current_task = task
        self.time_remaining = self.get_time_remaining()


class Task:
    def __init__(self, start_time):
        self.num_pages = random.randrange(1, 21)
        self.start_time = start_time
    
    def get_wait_time(self, end_time):
        return end_time - self.start_time


def new_task_created():
    return random.randrange(1, 181) == 180


def simulation(num_seconds, pages_per_minute):
    wait_times = []
    print_queue = Queue()
    printer = Printer(pages_per_minute)

    for current_time in range(num_seconds):
        if new_task_created():
            task = Task(current_time)
            print_queue.enqueue(task)
        if not printer.is_busy() and not print_queue.is_empty():
            current_task = print_queue.dequeue()
            wait_time = current_task.get_wait_time(current_time)
            wait_times.append(wait_time)
            printer.start_next_task(current_task)
        printer.tick()

    avg_wait_time = sum(wait_times) / len(wait_times)
    print(f"{avg_wait_time} seconds" + f"| {print_queue.size()}" + " tasks remaining")

for i in range(10):
    simulation(3600, 5)

"""
Pseudocode:
Use a for loop where each iteration is a second.
1. For each second, if a new task has been created (with its timestamp), enqueue it. 
2. If printer is not currently busy:
    a. Dequeue task at top of queue and start it
    b. Calculate the wait time by subtracting its start time from the current time, and append this time to a list
3. Else if printer is busy, work on current task
    a. Set printer current status to busy.
    b. Calculate total time to complete task based on number of pages
    c. Decrease total time by 1 for each second.
    c. If time remaining is 0, then set the current task to None, and the state to Not Busy.
4. Repeat steps 1-3 until end for loop
"""