import re
def is_indian_phone_number(number: str) -> bool:
    """
    Checks if the given string is a valid Indian phone number.
    Valid formats:
      - 10 digits starting with 6, 7, 8, or 9
      - Optional country code (+91 or 91) at the start
      - Optional spaces or hyphens
    Examples of valid numbers:
      +91 9876543210
      919876543210
      9876543210
      +91-9876543210

    Returns True if valid, False otherwise.
    """
    pattern = r'^(\+91[\-\s]?|91[\-\s]?)?[6-9]\d{9}$'
    return bool(re.match(pattern, number.strip()))