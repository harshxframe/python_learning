from multiprocessing import Process
import time


def sendEmail(email):
    print(f"EMail is sending.. to {email}")
    time.sleep(3)
    print(f"EMail send successfully. to {email}")


# Start
if __name__ == "__main__":

       sedEMail = [
           Process(target=sendEmail, args=(f"harsh@gmail.com{i}",))
           for i in range(3)
            ]

       #Start all process

       for e in sedEMail:
            e.start()


    #wait for all complete
       for e in sedEMail:
            e.join()

       print("All email  sent")
