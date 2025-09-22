# Calculate average score of a student
def calc_average(marks):
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average   # Fixed typo: was 'avrage'

marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))  # Fixed missing closing parenthesis
