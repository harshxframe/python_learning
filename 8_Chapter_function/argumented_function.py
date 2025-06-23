# function with argument


def great(name, ending):
    print("Good Day,",name)
    print(ending)


great("Harsh", "Thank you")
great("Akash", "Thank you")
great("Divya", "Thanks")





# handling a function if function returning a value

def result(marks):
    if marks <33:
        return "Failed try next time"
    else:
        return "Passed congratulations"


finalResult  = result(23)
print(finalResult)


# default argument

def greyGreeting(name, surname="Mr"):
    print("Hello",surname,name)



greyGreeting("Harsh", "He")