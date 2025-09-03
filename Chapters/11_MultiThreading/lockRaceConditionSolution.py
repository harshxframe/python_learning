import threading
import time

finalAmount = 100
Lock = threading.Lock()


def withdraw(requestedAMount):
    global finalAmount
    with Lock:
        temp = finalAmount - requestedAMount
        time.sleep(2)
        finalAmount = temp
        print(f"Withdrawing {requestedAMount} from {finalAmount}")



task1 = [threading.Thread(target=withdraw, args=(30,)) for i in range(3)]
for t in task1:
    t.start()

for t in task1:
    t.join()



