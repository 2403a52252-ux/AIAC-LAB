# Original complex nested if-else logic simplified using elif
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Alternative approach using dictionary mapping for even cleaner code
def grade_with_mapping(score):
    # Define grade boundaries and corresponding grades
    grade_boundaries = [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (0, "F")
    ]
    
    # Find the appropriate grade based on score
    for min_score, grade_letter in grade_boundaries:
        if score >= min_score:
            return grade_letter
    
    return "F"  # Fallback for negative scores

# Example usage and testing
if __name__ == "__main__":
    test_scores = [95, 85, 75, 65, 55, 100, 0]
    
    print("Testing simplified elif version:")
    for score in test_scores:
        print(f"Score {score}: Grade {grade(score)}")
    
    print("\nTesting dictionary mapping version:")
    for score in test_scores:
        print(f"Score {score}: Grade {grade_with_mapping(score)}")
