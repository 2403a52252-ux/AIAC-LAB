def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Error: Negative number"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Calculate factorial of 8
result = factorial(8)
print(f"Factorial of 8 = {result}")
