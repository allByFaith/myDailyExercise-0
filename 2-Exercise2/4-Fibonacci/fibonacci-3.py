import sys

def fibonacci_of(n):
    sys.setrecursionlimit(2000)
    
    try: 
        # print(fibonacci_of(n))
        if n in {0, 1}:  # Base case
            return n
        else:
            return (fibonacci_of(n - 1) + fibonacci_of(n - 2))
    except Exception as e:
        print(e)

def main():

    print(fibonacci_of(40))

main()