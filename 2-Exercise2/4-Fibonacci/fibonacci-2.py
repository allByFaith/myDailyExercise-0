# ============================
# Refer to Solution 2
# ============================

# Let's add memoisation so that before we work out fib(n), 
# we check if we've already done the work and if so return 
# the result instead

# The maximum recursion depth in Python is 1000.
import sys
import traceback

def fast_fib(n: int, memo: dict = {}) -> int:
    
    # print(sys.getrecursionlimit()) # The limitation is 1000, so use below
    # sys.setrecursionlimit(n) where n = 2000 to extend the MAX recursion limitation
    sys.setrecursionlimit(2000)

    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)

    return memo[n]

def main():
    try:
        getNumberFromUser = input("Please enter a number :- ")
        result = fast_fib(int(getNumberFromUser))
        print(f"The result of the Fibonacci number for your input {getNumberFromUser} is {result}")
    except Exception as e:
        traceback.print_exc()
        print(e)
        pass

main()

# # That was fast:
# print(fast_fib(100))

# # So was this:
# print(fast_fib(1000)) # Will have to extend max recursion dept to go beyond this