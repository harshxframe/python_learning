# define the generator





def callRequest():
    yield "Make request for send email"    # Here when a call once it become pase on that state and resume where it has paused. Does not exist from memory still in memory with privious state
    yield "Make phone call notification"
    yield "Make a in device notification"



stall = callRequest()    # It just holds the reference of the function
print(next(stall))  # Way to call one by one because it began where it was paused
print(next(stall))
print(next(stall))


for cup in stall:   # One of the way to use
    print(cup)






# We need to take care of that

# 1. Yield
# 2. next() run a Yield
# 3. send() send a value in yield
# 4. yield from function()  pass a function as task
# 5. close() close the yield and cleanup memory


