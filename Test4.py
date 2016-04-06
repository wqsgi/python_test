import _thread
from queue import Queue
import time

__author__ = 'weiqisong'


def printTime():
    while True:
        time.sleep(1)
        print(time.strftime("%Y-%m-%d %H:%M:%S"))



#_thread.start_new(printTime(),("",""))

queue = Queue()

def producer():
    while True:
        time.sleep(1)
        yield queue.put(time.strftime("%Y-%m-%d %H:%M:%S"))

def consumer():
    yield print(queue.get())
