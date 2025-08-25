import re
from collections import Counter

def analyze_word_frequency(text):
    """Return the most frequently used word in the given text."""
    # Convert to lowercase, remove punctuation, split into words
    words = re.sub(r'[^\w\s]', '', text.lower()).split()
    return Counter(words).most_common(1)[0][0] if words else ""

# Test cases
if __name__ == "__main__":
    test_cases = [
        "rain rain go away",
        "I can dance,I can walk,I can run,eat,sleep", 
        "vyshu is a brilliant,intelligent ,and vyshu is a multitalent vyshu can do anything",
        "python is amazing python is powerful python is versatile python programming"
    ]
    
    for text in test_cases:
        result = analyze_word_frequency(text)
        print(f"Input: {text}")
        print(f"Output: {result}\n")
