# Python 2 Exercises

## Loops

# 1. Print the numbers 0 to 10 using a for loop.
# 1. Print the numbers 0 to 10 using a while loop.
# 1. Print the list of numbers below using a for loop.

#     ```py
#     nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
#     ```

# 1. Print the message 'Done!' after printing the numbers 0 to 10 with a for loop. Hint: use the `for-else` construct.
# 1. Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of the element.

#     ```py
#     list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
#     list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
#     ```

# 1. Using a while loop, on every iteration generate a random number. 
# If it's a multiple of 5, __break__ from the loop. If it's a multiple of 3, 
# end the current iteration with __continue__ and print a message to show you are skipping. 
# If it's neither, print the number and continue the loop.

#     When the loop has been broken, print a message indicating that this has happened before the program exits.

#     Hint:

#     ```py
#     import random
#     x = random.randint(1,100)
#     ``` 

def printFor1():
    for x in range(0, 11):
        print("x->", x)
    else:
        print("Done!")

def printWhile1():
    loopCount = 0
    while (loopCount <=10):
        print("Count -> ", loopCount)
        loopCount += 1
    print("Done!")

def printList1():
    # Create a list : nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
    nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
    for item in nums:
        print("The list item : ", item)
    print("Done!")

# Print item that were found in the two given lists
# list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
# list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
def itemMatch():
    list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
    list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
    
    countMatchedItem = 0

    print("List1 -> ", list1)
    print("List2 -> ", list2)
    for x in list1:
        for y in list2:
            if (x == y):
                print("Match Item -> ", x)
                countMatchedItem += 1
            else:
                continue
    
    if (countMatchedItem > 0):
        print(f"There are {countMatchedItem} matched in the above two given lists!")

def main():
    # Testing, run the following function one by one
    #       printFor1()
    #       printWhile1()
    #       printList1()
    #       itemMatch()
    pass

main()
