# by extending Threading class

from locale import currency
import threading
import time

class mythread(threading.Thread):
    def run(self):
        for x in range(7):
            print("hi from child",threading.current_thread().getName())
a=mythread()
a.start()
time.sleep(1)
print("bye",threading.current_thread().getName())