# seeing the way of passing value in the generators


def mainSend():
    print("Welcome how much you want to pay!")
    order = yield
    while True:
        print("order processing")
        order = yield



agent = mainSend()
next(agent) # start the generator
agent.send("Cars")
agent.send("Aeroplanes")
