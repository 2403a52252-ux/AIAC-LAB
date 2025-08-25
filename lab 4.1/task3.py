def parse_student_info(student_dict):
    full_name = student_dict.get('full name', 'Unknown')
    branch = student_dict.get('branch', 'Unknown')
    cgpa = student_dict.get('cgpa', 'Unknown')
    return f"Student: {full_name}, Branch: {branch}, CGPA: {cgpa}"
# Example 1
student1 = {
    'full name': 'challa vyshu',
    'branch': 'cse',
    'cgpa': 9.8
}
# Example 2
student2 = {
    'full name': 'pandu reddy',
    'branch': 'ECE',
    'cgpa': 10
}
# Example 3 (new one)
student3 = {
    'full name': 'sneha kumari',
    'branch': 'IT',
    'cgpa': 9.5
}
print(parse_student_info(student1))
print(parse_student_info(student2))
print(parse_student_info(student3))