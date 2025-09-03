# Write a program to find python word in log file and return the number of line where python word is present




with open("python_log.txt", "r+") as logFile:
        numberLine = 1
        found = False
        for line in logFile:
            if "python" in line:
                found = True
                print("python found on line no: ",numberLine)
            numberLine +=1
        if not found:
            print("No python found in Log File")


