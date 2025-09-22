def welcome_student(student_name):
    """Print a welcome message for a student."""
    print("Welcome", student_name)
def welcome_all_students(students_list):
    """Print welcome messages for all students in the list."""
    for student in students_list:
        welcome_student(student)
# Sample usage
students = ["Alice", "Bob", "Charlie"]
# Method 1: Using the welcome_all_students function
welcome_all_students(students)
# Method 2: Alternative - using list comprehension (if you want a more concise approach)
# [welcome_student(student) for student in students]
# Method 3: Alternative - using map function
# list(map(welcome_student, students))
