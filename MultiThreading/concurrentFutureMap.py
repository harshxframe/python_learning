import concurrent.futures
import time


def sendEmail(emails):
    print("Email is sending...! to ...", emails)
    time.sleep(4)
    print("Email send successfully!")
    return True



timeFrame1 = time.perf_counter()


email =["e@gmail.com", "harsh@gmail.com", "m@gmail.com", "krisha@gmail.com"]


with concurrent.futures.ThreadPoolExecutor(max_workers=len(email)) as executor:
    tasks = executor.map(sendEmail, email)



for task in tasks:
      print("Email send: ",task)

timeFrame2 = time.perf_counter()
executionTime = timeFrame2 - timeFrame1


print(executionTime)
