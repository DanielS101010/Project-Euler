limit = 4000000

a = 1
b = 1
sum_even_fib = 0

while b < limit:
    if b % 2 == 0:
        sum_even_fib += b
    # Update the Fibonacci sequence correctly
    a, b = b, a + b

print(sum_even_fib)

