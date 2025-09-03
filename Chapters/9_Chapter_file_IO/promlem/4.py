# Written a program to check whether appropriate Word is present or not if yes replacing the word by hashing


def replaceWord(story):
    if story.__contains__("Donkey"):
        ProcessedStory = story.replace("Donkey", "#######")
        return ProcessedStory
    elif story.__contains__("donkey"):
        ProcessedStory = story.replace("donkey", "#######")
        return ProcessedStory
    else:
        return False



with open("DonkeyStory.txt", "r+") as f:
    data = f.read()
    ReplacedStory = replaceWord(data)
    if ReplacedStory != False:
        f.seek(0)
        f.truncate()
        f.write(ReplacedStory)
        print("ReplacedStory operation done!")
    else:
        print("Appropriate word not found!")
