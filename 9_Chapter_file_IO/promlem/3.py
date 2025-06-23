# Write a program to create a table 1 to 20 and save tables in each file.

import os


folderPath = "/Users/harsh/python_learning/9_Chapter_file_IO/promlem/tables/"
tableList = []
tableNaming = 0

def createFolder():
    if os.path.exists(folderPath):
        return True
    else:
        os.makedirs(folderPath)
        return False


def createAndSavefile(data, name="table"):
    fullPath = os.path.join(folderPath, name)
    with open(fullPath, "w") as f:
        f.seek(0)
        f.write(str(data))

    return True


def createTable():
    global tableList
    tableLen =1
    while tableLen <= 20:
        i = 1
        while i <= 10:
            tLine = f"{tableLen}*{i} = {tableLen*i}"
            tableList.append(tLine)
            i+=1

        table = "\n".join(tableList)
        tableName = "table" + str(tableLen)
        FileSaved = createAndSavefile(table, tableName)
        print(FileSaved, "of", "Table ", i)
        tableList = []
        tableLen += 1



#Main execution starting from here...

createTable()
