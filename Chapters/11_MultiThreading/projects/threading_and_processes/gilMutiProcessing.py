import threading
from multiprocessing import Process
import time



def read():
    print("Reading...")
    counter = 0
    for _ in range(100_000_000):
        counter += 1
    print("Ended the counter",counter)



if __name__ == "__main__":
         print("Code execution started.")
         timeFrame1 = time.perf_counter()
         processes1 = Process(target = read)
         processes2 = Process(target = read)
         processes1.start()
         processes2.start()

         processes1.join()
         processes2.join()


         print("Code execution ended.")
         timeFrame2 = time.perf_counter()
         timeTotal = timeFrame2 - timeFrame1
         print("Total execution time:", timeTotal)



