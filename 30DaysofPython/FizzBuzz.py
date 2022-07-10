# Find all numbers in 100
# For all numbers dividable by 3 print Fizz
# For all numbers dividable by 5 print Buzz
# For all numbers dividable by 3 & 5 print FizzBuzz
# TIP: Do the 3&5 first or their will be none found!


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz!")
    elif number % 5 == 0:
        print("Buzz!")
    elif number % 3 == 0:
        print("Fizz!")
    else:
        print(number)