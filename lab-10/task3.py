def calculate_percentage(base_value, percentage_rate):
    """
    Calculate a percentage of a given base value. 
    Args:
        base_value (float): The base value to calculate percentage from
        percentage_rate (float): The percentage rate to apply (e.g., 15 for 15%)  
    Returns:
        float: The calculated percentage amount
    Example:
        >>> calculate_percentage(200, 15)
        30.0
    """
    # Calculate percentage by multiplying base value with rate and dividing by 100
    return base_value * percentage_rate / 100
# Define the base amount for calculation
base_amount = 200
# Define the percentage rate to calculate (15%)
percentage_rate = 15
# Calculate and print the result (15% of 200)
print(calculate_percentage(base_amount, percentage_rate))
