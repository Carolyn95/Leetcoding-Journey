# Mutl-Threading example
from threading import Thread
import os
import math


def calc():
  for i in range(0, 4000000):
    math.sqrt(i)


threads = []

for i in range(os.cpu_count()):
  print('registering thead %d' % i)
  theads.append(Thread(target=calc))

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

# Multi-processing example
from multiprocessing import Process
import os
import math


def calc():
  for i in range(0, 4000000):
    math.sqrt(i)


processes = []

for i in range(os.cpu_count()):
  print('registering process %d' % i)
  processes.append(Process(target=calc))

for process in processes:
  process.start()

for process in processes:
  process.join()
