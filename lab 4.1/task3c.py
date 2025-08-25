def parse_student(student_dict):
    """Parse student information from dictionary"""
    return {
        'name': student_dict.get('full name', '').strip(),
        'branch': student_dict.get('branch', '').strip().upper(),
        'cgpa': float(student_dict.get('cgpa', student_dict.get('CGPA', 0)))
    }
# Examples
student1 = {'full name': 'challa vyshu', 'branch': 'cse', 'cgpa': 9.8}
student2 = {'full name': 'pandu reddy', 'branch': 'ECE', 'CGPA': 10}
student3 = {'full name': 'sai kumar', 'branch': 'mechanical', 'cgpa': 8.5}
# Display results
for i, student in enumerate([student1, student2, student3], 1):
    parsed = parse_student(student)
    print(f"Student {i}: {parsed}")
