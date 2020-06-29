# Program to return the Nth fibonacci number entered as an argument
# Usage: $ python FastFibonacci.py Nth 
# Example: "python FastFibonacci.py 100" will return the 100th fibonacci number.

import sys


# returns F(n)
def fibonacci(n: int):  # noqa: E999 This syntax is Python 3 only
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]


# returns (F(n), F(n-1))
def _fib(n: int):  # noqa: E999 This syntax is Python 3 only
    if n == 0:
        return (0, 1)
    else:
        # F(2n) = F(n)[2F(n+1) − F(n)]
        # F(2n+1) = F(n+1)^2+F(n)^2
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Too few or too much parameters given.")
        exit(1)
    try:
        n = int(args[0])
    except ValueError:
        print("Could not convert data to an integer.")
        exit(1)
    print("F(%d) = %d" % (n, fibonacci(n)))


main(n)