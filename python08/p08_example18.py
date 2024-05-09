# Tuples: Student information

# Create a tuple for student details (name, age, grade)
student = ("Alice", 18, "A")

# Accessing elements
name = student[0]
age = student[1]
grade = student[2]

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Grade: {grade}")

# Unpacking a tuple
name, age, grade = student  # Assigning elements to separate variables

print("\nUnpacked student details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Grade: {grade}")

# Modifying a tuple (not possible)
# student[1] = 19  # This will cause an error!

# Creating a new tuple with changes
new_student = (name, 19, grade)  # Modify age
print("\nNew student details (modified age):")
print(f"Name: {new_student[0]}")
print(f"Age: {new_student[1]}")
print(f"Grade: {new_student[2]}")
