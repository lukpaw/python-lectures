# Define a tuple to store course information (name)
courses = ("Math", "Physics", "English")

# Create a dictionary to store student information (name, ID, enrolled_courses)
students = {
    "Alice": {
        "ID": 12345,
        "enrolled_courses": []  # List to store enrolled courses as strings (course name)
    },
    "Bob": {
        "ID": 54321,
        "enrolled_courses": []
    }
}

# Enroll Alice in Math and English courses
students["Alice"]["enrolled_courses"].append(courses[0])  # Math
students["Alice"]["enrolled_courses"].append(courses[2])  # English

# Enroll Bob in Physics
students["Bob"]["enrolled_courses"].append(courses[1])  # Physics

# Print student information
for student_name, student_data in students.items():
    print(f"\nStudent Name: {student_name}")
    print(f"  ID: {student_data['ID']}")
    print(f"  Enrolled Courses:")
    for course in student_data["enrolled_courses"]:
        course_name = course
        print(f"    - {course_name}")
