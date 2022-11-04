# File Name     : tryExceptFinal.py
# Author        : Samuel KO
# Date          : 26 Oct 2022
# Description   : Use the below list to write all names to a file where
#                 each name is on a new line.
#                 
#                 myList = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
#
#               : Use try..except..finally

# Input         : Read the above given list as input
# Output        : Write all names to a file (each name is on a new line)
# 

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

file_exists = exists(workFile)
try:
    if(file_exists):
        fileHandle = open(workFile, "w") # Open a file for writing
    else:
        fileHandle = open(workFile, "x") # Create a file for writing

    for name in myList:
        itemToWrite = name + '\n'
        fileHandle.write(itemToWrite)
        
except Exception as e:
        print("Error : " + e + ".")
finally:
    # Close the file "nameFile"
    fileHandle.close()

    # Print the original list's contents   
    print(f"The Original List : {myList}")

    print("\nAfter writing, print the contents of file " + workFile + " : ")
    # Execute the console command
    system('cat ' + workFile)