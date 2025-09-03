letter = '''Dear <!Name>,
you are selected!, <!date>'''

 
name = letter.replace("<!Name>", "Harsh"). replace("<!date>", "24/sep/2050") # this is called chaining


print(name)