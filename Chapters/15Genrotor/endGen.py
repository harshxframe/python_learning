# Now how to end the generator from the memory

# Yield from close

def main():
    yield "S-class Car"
    yield "BMW 7 Series"


def sportsCar():
    yield "Lamborghini"
    yield "Proses"


def makeCarOrder():
    yield from sportsCar()
    yield  from main()

for order in makeCarOrder():
    print(order)



# how to close order

def orderControl():
    try:
        while True:
            NreOrder = yield "Waiting for the order"

    except Exception as e:
        print("Order closed now more car left")


orderTable = orderControl()
print(next(orderTable))
orderTable.close()
