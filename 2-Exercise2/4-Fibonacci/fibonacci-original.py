# Function Name : fibonacci-original.py
# input         : An integer (User input)
# Date          : 24 Oct 2022
# Author        : Samuel KO
# Description   : Implement the fibonacci sequence
#                 The fibonacci sequence is the sum of the previous two values
#                 1, 1, 2, 3, 5, 8, 13...
# Return        : Result
# n =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
# Xn =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	...
# Bonus         : Create a fibonacci function that returns fib(n) . So if i request fib(100) 
# it returns the 100th position in the sequence. n is undetermined so working out a finite 
# sequence beforehand is not acceptable ;)

import sys
import traceback

def fibonacci1(n):
    if n == 0:
       return 0
 
    if n == 1:
       return 1
 
    return fibonacci1(n - 1) + fibonacci1(n - 2)

def main():
    # set the MAX recursion limit to 2000
    sys.setrecursionlimit(2000)

    inNum = int(input("Please enter a number to gen fibonacci number : "))
    try:
        result = fibonacci1(inNum)
    except:
        traceback.print_exc()

    print(result)

main()

