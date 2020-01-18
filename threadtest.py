import threading
import sys
import time

def task(j):
    time.sleep(j)
    print('hoge')
    # sys.exit(0)
    raise RuntimeError("error!!")

ths = []
for i in range(5):
    t = threading.Thread(target=task, args=(i, ))
    ths.append(t)
    t.start()

for t in ths:
    t.join()

