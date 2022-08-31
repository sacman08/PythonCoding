# Write a program that finds the highest square lower than a certain number
import math
# Whats the number?
max_num = int(input("Please enter an integer for test:"))
# Calculate the square and find highest
print(f"Highest square for {max_num} is {math.isqrt(max_num) * math.isqrt(max_num)} ({math.isqrt(max_num)} doubled).")
# Return solution
for num in range(max_num):
    square_num = num ** 2
    if square_num > max_num:
        break
    print(f'{num ** 2}')