class Train:
    def __init__(self):
        self.seats = 2000
        self.fare = 24000

    def getStatus(self):
        return  self.seats

    def bookSeat(self, seats):
        if self.seats>=seats  :
           self.seats = self.seats-seats
           return "Your seat Booked"
        else:
           return "Seats Not Available"

print("Welcome to Harsh Railway!")


train = Train()

while True:
    print("Enter 1 to getStatus!")
    print("Enter 2 to book seats!")

    inp = int(input("Enter your choice: "))
    if inp==1:
     print("Available seats: ",train.getStatus())
    else:
     seatCount = int(input("Enter your seat count: "))
     print(train.bookSeat(seatCount))