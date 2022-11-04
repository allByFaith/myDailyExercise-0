# Simple Calculator
import sys

def add():
    num1 = float(input("please enter 1st number to add: "))
    num2 = float(input("please enter 1st number to add: "))
    return (num1 + num2)

def subtract():
    num1 = float(input("please enter 1st number to subtract : "))
    num2 = float(input("please enter 1st number to subtract : "))
    return (num1 - num2)

def multiply():
    num1 = float(input("please enter 1st number to multiply : "))
    num2 = float(input("please enter 1st number to multiply : "))
    return (num1 * num2)

def divided():
    num1 = float(input("please enter 1st number to divided: "))
    num2 = float(input("please enter 1st number to divided: "))
    return (f"{num1 / num2}")

def main():
    keepOn = True
    
    print("Welcome to the simple calculator")
    while keepOn:
        print("  1)--Add")
        print("  2)--Subtract")
        print("  3)--Multiply")
        print("  4)--Divided")
        print("  5)--Clear")
        print("  9)--Exit Calculator")
        try:
            choice = int(input("Please enter your choice:- "))
            if (choice == 9):
                print("Thank you, bye~")
                keepOn = False
            elif (choice == 1):
                result = add()
            elif (choice == 2):
                result = subtract()
            elif (choice == 3):
                result = multiply()
            elif (choice == 4):
                result = divided()
        except:
            # print("Oops!", sys.exc_info()[0], "occurred.")
            print("Oops, wrong input of \'" + str(choice) + "\' !!!!")
            print("Please re-enter again!")
        
        if (choice != 9):
            print(f"The result is {result}")
            result = 0
            print("Continue the calculation")

main()