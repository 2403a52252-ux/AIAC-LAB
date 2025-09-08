def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
    Returns:
        int or None: The nth Fibonacci number, or None if n is negative.
    """
    # The Fibonacci sequence is defined as:
    # F(0) = 0, F(1) = 1
    # F(n) = F(n-1) + F(n-2) for n > 1
    if n < 0:
        # Return None for negative input instead of raising an error
        return None
    if n == 0:
        return 0  # Base case: 0th Fibonacci number is 0
    elif n == 1:
        return 1  # Base case: 1st Fibonacci number is 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage:
if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer to find its Fibonacci number: "))
        result = fibonacci(n)
        if result is not None:
            print(f"The {n}th Fibonacci number is {result}")
        else:
            print("Input must be a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")