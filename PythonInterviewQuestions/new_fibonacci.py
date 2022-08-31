# Gives us fibonacci up to the nth number

def fib():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second


def fibn(number):
    for index, each_num in enumerate(fib()):
        if index == number:
            return each_num


try:
    calc_fib = int(input("How many numbers to calculate fibonacci? "))
    print(fibn(calc_fib))
except ValueError:
    print("Please enter a number!")
