# Generators



# Yield is a keyword



# Advantage

# 1. YOu save memory
# 2. YOu don't want result immediately



def callRequest():
    yield "Make request for send email"
    yield "Make phone call notification"
    yield "Make a in device notification"


stall = callRequest()

for cup in stall:
    print(cup)



