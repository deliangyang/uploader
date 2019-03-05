import threading
import time
import logging


class Counter(object):

    def __init__(self, start=0):
        self.value = start
        self.lock = threading.Lock()

    def increment(self, i):
        self.lock.acquire()
        try:
            if self.value <= 8:
                time.sleep(2)
            self.value = self.value + i
        finally:
            logging.info("current value: %s" % self.value)
            self.lock.release()

    def decrement(self):
        self.lock.acquire()
        try:
            self.value = self.value - 1
        finally:
            self.lock.release()

    def get(self):
        return self.value
