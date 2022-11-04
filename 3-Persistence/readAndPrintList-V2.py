# File Name     : readAndPrintList-V2.py
# Author        : Samuel KO
# Date          : 26 Oct 2022
# Description   :
#     1. Create a text file in your text editor and add some names of people on each line
#     2. Read the names from the file in your application and populate an empty 
#        ist with the names
#     3. Print out the list!
#     4. Did you notice something weird (use the .replace() function to do that!)

# Open a file for read
f = open("nameFile.txt", "r+")

# Create a empty list
myList = []

lineReadingObj = f.readlines()

for readName in lineReadingObj:
    x = readName.replace("\n", "")  # we can use strip() function here as well
    myList.append(x) # Add to the list

print(myList)