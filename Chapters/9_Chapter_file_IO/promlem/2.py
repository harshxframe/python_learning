

userNewScore = 345


with open("game_score.txt", "r+") as f:
     data = f.read()
     print("PreScore:", data)
     saveNewScore = int(userNewScore) + int(data)

     f.seek(0)  # cursor position
     f.truncate() # set null and clear the file
     f.write(str(saveNewScore))

     f.seek(0)
     finalScore = f.read()
     print(finalScore)







