# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# 10. Chat Simulator (OOP + AsyncIO + File I/O)
#
# Simulate a small chat between users.
#
# Each user runs as an async task sending messages with delay.
#
# Save all chat messages into a file.
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import time
count = 1
while True:
    count +=1
    print("Hello Harsh?",count)
    time.sleep(2)