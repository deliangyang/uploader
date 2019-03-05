import unittest
from uploader.worker.upload import items
from uploader.worker.counter import Counter
from uploader.worker.mutil_add import MultiAdd
import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

import threading


class TTest(unittest.TestCase):

    def test_tomal(self):
        self.assertIn('source', items)

    def test_thread(self):
        logging.info("current value: 1")
        counter = 0 #Counter()
        lock = threading.Lock()
        for i in range(100):
            thread = MultiAdd(counter, i, lock)
            thread.start()
