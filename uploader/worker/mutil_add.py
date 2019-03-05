import threading
import time


class MultiAdd(threading.Thread):

    def __init__(self, counter, i, lock):
        self.counter = counter
        self.value = i
        self.lock = lock
        threading.Thread.__init__(self)

    def run(self):
       # self.lock.acquire()
        # time.sleep(1)
        self.counter += self.value
        print(self.counter)
        # self.lock.release()
        # self.counter.increment(self.value)
