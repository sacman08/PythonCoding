# Find all numbers in 100
# For all numbers dividable by 3 print Fizz
# For all numbers divisable by 5 print Buzz
# For all numbers divisable by 3 & 5 print FizzBuzz


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz!")
    elif number % 5 == 0:
        print("Buzz!")
    elif number % 3 == 0:
        print("Fizz!")
    else:
        print(number)