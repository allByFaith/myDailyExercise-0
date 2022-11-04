# File Name     : writeDictionaryToFile.py
# Author        : Samuel KO
# Date          : 26 Oct 2022
# Description   : Use the names stored in repeatName.txt file to create a dictionary
#                 The file content :
#
#                 John
#                 James
#                 John
#                 Sally
#                 John
#                 Sally
#                 Mark
#                 John
#                   
#               : Use the file context manager and try..except..finally
#
# Input         : Read the above given name from file as input
# Output        : Write all names as key and the number of count of the name
#                 as the value to build a dictionary (myDict in the program)

# Create a newList to store the "clean" name which
# read from repeatName.txt file
newList = []

# empty dictionary
myDict = {}

try:
    f1 = open("repeatName.txt", "r")

    with open("repeatName.txt", "r") as f1:
            nameRead = f1.readlines()

    # clean up the list by removing the trailing "\n" character 
    for item in nameRead:
        # Read in each item from nameRead object, write it to newList object
        newList.append(item.strip("\n"))

    newList.sort()
    # print(newList)
    mySet = set(newList)
    # print(mySet)

    count = 0   # loop counter
    key = 0     # key variable for myDict
    value = 0   # value variable for myDict

    for key1 in mySet:
        for key2 in newList:
            if (key1 == key2):
                count += 1
                # print(f"{x} --> {count}")
        key = key1  # set the key for myDict
        value = count   # set the value for myDict corresponding to the above key
        myDict[key] = value  # add to the myDict dictionary
        # print(f"{key}:{value}")
        count = 0  # reset the counter for next trial
except Exception as e:
    print(e)
finally:
    print(f"The created dictionary : {myDict}")
    print("end building dictionary process!")