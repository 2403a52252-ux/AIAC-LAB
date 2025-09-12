def sum_even_odd(numbers):
 """
    Calculates the sum of even and odd numbers in a list.
    Args:
        numbers (list of int): List of integers to process.
    Returns:
        tuple: A tuple containing two integers:
            - Sum of even numbers.
            - Sum of odd numbers.
        """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
nums = input("Enter numbers separated by spaces: ")
nums_list = [int(x) for x in nums.split()]
even, odd = sum_even_odd(nums_list)
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)