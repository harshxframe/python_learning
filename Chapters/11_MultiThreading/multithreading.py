import threading
import time


def funk(second):
    print("Sleeping... for: \n", second)
    time.sleep(second)


time1= time.perf_counter()


#Normal code
# funk(2)
# funk(4)
# funk(7)
#


#same code using thread
t1 = threading.Thread(target=funk, args=[2])
t2 = threading.Thread(target=funk, args=[4])
t3 = threading.Thread(target=funk, args=[7])

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2 - time1)




