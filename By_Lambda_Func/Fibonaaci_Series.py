fib = lambda n: [0, 1] + [fib(i-1)[-1] + fib(i-2)[-1] for i in range(2, n)]

# Get input from user
n = int(input("Enter a number to generate the Fibonacci series: "))

# Generate and print the Fibonacci series
print(fib(n)[:n])