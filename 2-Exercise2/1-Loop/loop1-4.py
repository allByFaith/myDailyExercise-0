# Python 2 Exercises

## Loops

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
    itemMatch()

main()
