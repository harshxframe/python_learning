import random


#
# 1 for snake
# -1 for water
# 0 for gun

def numberPic():
    # to pic appropriate random number
    randNum = random.randint(-1, 1)
    return randNum


while True:
    computer = numberPic()
    youStr = input("Enter your choice[s, w, g]")
    youDic = {"s":1, "w":-1, "g":0}
    you = youDic[youStr]


    if computer == -1 and you ==1:
       print("You win")
    elif computer ==-1 and you == 0:
       print("You lose")
    elif computer ==1 and you == -1:
       print("you lose")
    elif computer ==1 and you == 0:
       print("You win")
    elif computer ==0 and you == -1:
       print("You lose")
    elif computer ==0 and you == 1:
       print("You lose")
    elif computer == you:
       print("It's a draw")
    else:
       print("Something went wrong")


