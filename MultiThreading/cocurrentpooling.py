import concurrent.futures
import threading
import time
from sys import exc_info


def fuck(second):
    print("Email is sending... to : ", second)
    time.sleep(2)
    print("EMail send successfully?")
    return True

timeFrame1 = time.perf_counter()

email = ["harsh@gmail.com", "ayushi@gmail.com"]

with concurrent.futures.ThreadPoolExecutor(max_workers=len(email)) as executor:
    tasks1 = executor.submit(fuck, email[0])
    tasks2 = executor.submit(fuck, email[1])

    print("Task Done", tasks1.result())
    print("Task Done", tasks2.result())

timeFrame2 = time.perf_counter()

executionTime = timeFrame2 - timeFrame1

print(executionTime)



