# Function Name : fibonacci-final.py
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
#                 it returns the 100th position in the sequence. n is undetermined so working 
#                 out a finite sequence beforehand is not acceptable ;)
# Reference Website :
#               https://realpython.com/fibonacci-sequence-python/

# Memoizing the Recursive Algorithm
# The Fibonacci function calls itself several times 
# with the same input. Instead of a new call every time, you can store the results 
# of previous calls in something like a memory cache. You can use a Python list to 
# store the results of previous computations. This technique is called memoization.

# Memoization speeds up the execution of expensive recursive functions by storing 
# previously calculated results in a cache. This way, when the same input occurs 
# again, the function just has to look up the corresponding result and return it 
# without having to run the computation again. You can refer to these results as 
# cached or memoized:

import sys

def fibonacci_of(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    # defines two local variables, previous and fib_number, and initializes 
    # them with the first two numbers in the Fibonacci sequence.
    previous, fib_number = 0, 1

    # starts a for loop that iterates from 2 to n + 1. The loop uses an underscore
    # (_) for the loop variable because it’s a throwaway variable and you won’t be 
    # using this value in the code.
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

def main():
    # Set the MAX of recursion limit to 2000
    sys.setrecursionlimit(2000)
    
    inNum = int(input("Please enter a number to gen fibonacci number : "))    
    result = fibonacci_of(inNum)
    print(result)

main()