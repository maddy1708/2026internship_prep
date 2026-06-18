# Dataset of employees
employees = [
    {"id": 1, "name": "Alice", "age": 25, "department": "Engineering", "salary": 75000},
    {"id": 2, "name": "Bob", "age": 32, "department": "Marketing", "salary": 55000},
    {"id": 3, "name": "Charlie", "age": 29, "department": "Engineering", "salary": 85000},
    {"id": 4, "name": "David", "age": 41, "department": "HR", "salary": 60000},
    {"id": 5, "name": "Eva", "age": 27, "department": "Engineering", "salary": 70000}
]

# conditions
MIN_SALARY = 70000
TARGET_DEPARTMENT = "Engineering"
MAX_AGE = 30

# List to store filtered records
filtered_employees = []


for employee in employees:
    
    if (
        employee["department"] == TARGET_DEPARTMENT
        and employee["salary"] >= MIN_SALARY
        and employee["age"] <= MAX_AGE
    ):
        filtered_employees.append(employee)
        
print("Filtered Employees:\n")

for employee in filtered_employees:
    print(employee)