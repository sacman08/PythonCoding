import matplotlib.pyplot as plt

squares = [1, 1, 3, 5, 8, 13, 21, 34, 55]
plt.plot(squares, linewidth=5)

# set chart title and label axes
plt.title('Fibonacci Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Fib Value', fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
