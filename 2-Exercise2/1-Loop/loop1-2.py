# Python 2 Exercises

## Loops

# 1. Print the numbers 0 to 10 using a while loop.

# 1. Print the message 'Done!' after printing the numbers 0 to 10 with a for loop. Hint: use the `for-else` construct.
# 1. Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of the element.

def printWhile1():
    loopCount = 0
    while (loopCount <=10):
        print("Count -> ", loopCount)
        loopCount += 1
    print("Done!")

def main():
    # Testing, run the following function one by one
    printWhile1()

main()
