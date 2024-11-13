# Given two sets of students in two different courses:
# Science = {"Alice", "Bob", "Cindy", "David"}
# S.Science = {"Bob", "Cindy", "Ella", "Frank"}
# Find students enrolled in both courses.
# Find students enrolled in either course but not both.
# Find students enrolled only in Science but not in S.Science.
# Add a new student "George" to both courses and update your results accordingly.
# Convert the result to a sorted list.

Science = {"Alice", "Bob", "Cindy", "David"}
SScience = {"Bob", "Cindy", "Ella", "Frank"}

# Enroll in Both
in_Both = Science.intersection(SScience)
print("Students Enrolled themself in both courses:",in_Both)

# Enroll in only one course
in_One = Science.symmetric_difference(SScience)
print("Students Register themself in one course:",in_One)

# Enroll in Course A only
in_Science= Science.difference(SScience)
print("Students Register themself in Science course only:",in_Science)

# Enroll new student in both Course
Science.add("Vishnu")
SScience.add("Vishnu")


in_both_updated = Science.intersection(SScience)
in_one_updated = Science.symmetric_difference(SScience)
in_Science_updated = Science.difference(SScience)

print(in_both_updated)
print(in_one_updated)
print(in_Science_updated)


