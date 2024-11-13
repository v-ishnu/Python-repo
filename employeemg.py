# Build a system to manage employee skills using a dictionary where:

# The key is the employee’s ID, and the value is a set of skills they have.
# Allow adding new skills to an employee and removing existing skills.
# Display all employees with a specific skill.
# List all skills for a given employee.
# Display all employees, with their skills sorted alphabetically by employee ID.
# Note: Track the years of experience for each skill as a dictionary value {skill: years_of_experience} and allow searching for employees with a specific skill and experience level.
employee_skills = {}

# Add employees
employee_skills["AI"] = {}
employee_skills["App Dev"] = {}
employee_skills["DevOps"] = {}

# Add skills
employee_skills["AI"]["Python"] = 5
employee_skills["App Dev"]["Java"] = 3
employee_skills["DevOps"]["Python"] = 2
employee_skills["DevOps"]["C++"] = 4
employee_skills["DevOps"]["JavaScript"] = 6

# Display all employees
print("All Employees:")
for employee_id in sorted(employee_skills.keys()):
    print(f"Employee ID: {employee_id}")
    for skill, experience in employee_skills[employee_id].items():
        print(f"- {skill}: {experience} years")
    print()

# Get employees with a specific skill
employees_with_python = [employee_id for employee_id, skills in employee_skills.items() if "Python" in skills]
print("Employees with Python:", employees_with_python)

# Get skills for a given employee
print("Skills for E001:", employee_skills.get("E001"))

# Get employees with a specific skill and experience level
employees_with_python_3_years = [
    employee_id 
    for employee_id, skills in employee_skills.items() 
    if "Python" in skills and skills["Python"] >= 3
]
print("Employees with Python and 3+ years of experience:", employees_with_python_3_years)

# Remove a skill
if "E001" in employee_skills and "Java" in employee_skills["E001"]:
    del employee_skills["E001"]["Java"]

# Display all employees again
print("All Employees after removal:")
for employee_id in sorted(employee_skills.keys()):
    print(f"Employee ID: {employee_id}")
    for skill, experience in employee_skills[employee_id].items():
        print(f"- {skill}: {experience} years")
    print()
