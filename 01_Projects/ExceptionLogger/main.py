
#This code can malfunction or implementation not as per given documentation.
#This code can malfunction or implementation not as per given documentation.
#This code can malfunction or implementation not as per given documentation.
#This code can malfunction or implementation not as per given documentation.
#This code can malfunction or implementation not as per given documentation.




######################################################################################



# 9. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Exception Logger (Multithreading + Exception Handling)
#
# Create a program where multiple threads perform random operations (divide numbers, add numbers).
#
# If exceptions occur, log them into a file using a daemon thread.
import threading
import time
from time import sleep

addLog = []
divideLog = []

def divide():
    a1 = [34, 45, 56, 23, 67, 89, 456, 234, 453, 556]
    t1 = [3, 4, 6, 4, 8, 1, 5, 5, 2, 6]
    for i in a1:
        for j in t1:
            result = i / j
            divideLog.append(f"DIVIDE LOG: {i}/{j}={result}")
            time.sleep(2)


def add():
      a1 = [34,45,56,23,67,89,456,234,453,556]
      t1 = [3,4,6,4,8,1,5,5,2,6]
      for i in a1:
          for j in t1:
              result = i+j
              addLog.append(f"ADD LOG: {i}+{j}={result}")
              time.sleep(2)


def logger():
    while True:
            print(addLog[len(addLog)-1])
            time.sleep(2)






def bgLogger():
    t1 = threading.Thread(target=divide, args=[])
    t2 = threading.Thread(target=add, args=[])
    t3 = threading.Thread(target=logger, args=[])
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()




daemonBgThread = threading.Thread(target=bgLogger, args=[], daemon=True)
daemonBgThread.start()


print("Non blocked code!")
daemonBgThread.join()