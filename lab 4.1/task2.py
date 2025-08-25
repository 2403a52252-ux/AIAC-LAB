def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Find factorial of 8
print(factorial(8))  # Output: 40320