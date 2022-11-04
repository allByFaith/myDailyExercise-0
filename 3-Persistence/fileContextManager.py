# A context manager usually takes care of setting up some resource, 
# e.g. opening a connection, and automatically handles the clean up 
# when we are done with it. Probably, the most common use case is 
# opening a file. with open('/path/to/file.txt', 'r') as f: for line 
# in f: print(line)
#
# File Name     : fileContextManager.py
# Author        : Samuel KO
# Date          : 26 Oct 2022
# Description   : Use the below list to write all names to a file where
#                 each name is on a new line.
#                 
#                     myList = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
#
#               : Use the file context manager to take care of setting up
#                 the resource such as open a file here
# 
# Input         : Read the above given list as input
# Output        : Write all names to a file (each name is on a new line)

# impot os for path module
from os.path import exists 

# import only system from os
from os import system

# Give the name of workFile variable
workFile = "nameFile"

# Create a name list
myList = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# Clear the console
cleanConsole = system('clear')

# Check if the file "nameFile" is existed
file_exists = exists(workFile)

try:
    if(file_exists == False):
        fileHandle = open(workFile, "x") # Create a file for writing

    with open(workFile, "w") as fileHandle:
        for name in myList:
            itemToWrite = name + '\n'
            fileHandle.write(itemToWrite)
        
    # Close the file "nameFile" after finish writing
    fileHandle.close()

    # Print the original list's contents   
    print(f"The Original List : {myList}")

    print("\nAfter writing, print the contents of file " + workFile + " : ")
    # Execute the console command
    system('cat ' + workFile)

except Exception as e:
        print("Error e : ", e)