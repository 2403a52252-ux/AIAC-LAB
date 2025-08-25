import string
from collections import Counter
def most_frequent_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = paragraph.split()
    # Count word frequency
    freq = Counter(words)
    # Return the most common word
    return freq.most_common(1)[0][0]

# Example for you:
example = "Python is fun, and python is powerful. Python can do many things, and python is easy to learn."
print(most_frequent_word(example))  # Expected output: python
