def sum(inNum1, inNum2):
    return (inNum1 + inNum2)

def main():
    num1 = int(input("Please enter a first integer number :- "))
    num2 = int(input("Please enter a second integer number :- "))

    result = sum(num1, num2)
    print(f"{num1} + {num2} = {result}")

main()
