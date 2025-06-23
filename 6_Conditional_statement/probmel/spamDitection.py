scamKeyword = ["Make a lot money", "buy now", "subscribe now", "click this"]
message = "Hey, thanks for it option to Make a lot money"


# check that if message contain this word
newMessage = message.upper()





if newMessage.__contains__(scamKeyword[0].upper()) or newMessage.__contains__(scamKeyword[1].upper()) or newMessage.__contains__(scamKeyword[2].upper()) or newMessage.__contains__(scamKeyword[3].upper()):
    print("This message might be scam please be carefull")
else:
    print("Message is safe procced for futher action")
