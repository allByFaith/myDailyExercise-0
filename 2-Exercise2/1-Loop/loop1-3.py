# Python 2 Exercises

## Loops

# 1. Print the list of numbers below using a for loop.

#     ```py
#     nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
#     ```

def printList1():
    # Create a list : nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
    nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
    for item in nums:
        print("The list item : ", item)
    print("Done!")

def main():
    # Testing, run the following function one by one
    printList1()

main()
