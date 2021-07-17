from threading import Thread, Event
from time import time, sleep
from random import random

def process(x):
    sleep(x)
    print("done")

class Connection_with_timeout:

    def __init__(self, timeout):
        self.timeout = timeout
        self.current_time = self.start_time = time()
        self.breaks = Event()
        self.clock = Thread(target=self.timestep)
        self.clock.start()
        
    def timestep(self):
        while True:
            if self.breaks.isSet():
                print("Timer Stop")
                break
            sleep(1)
            self.current_time += 1

    def iter(self):
        if self.current_time - self.start_time > self.timeout:
            raise Exception("Time Out!")
        return random()

    def next(self):
        i = self.iter()
        self.start_time = time()
        return i

    def stop_thread(self):
        self.breaks.set()
