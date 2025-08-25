import re

def is_indian_phone_number(phone_number):
    """Check if phone number is a valid Indian phone number."""
    # Remove non-digits except + and check pattern
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    return bool(re.match(r'^(\+91)?[2-9]\d{9}$', cleaned))

# Example usage
if __name__ == "__main__":
    # Test cases
    test_numbers = [
        "+91 98765 43210",    # Valid
        "9876543210",         # Valid
        "1234567890",         # Invalid (starts with 1)
        "0123456789",         # Invalid (starts with 0)
        "987654321",          # Invalid (9 digits)
    ]
    
    for number in test_numbers:
        print(f"{number} -> {'Valid' if is_indian_phone_number(number) else 'Invalid'}")
