# Employee Management Program
# Filters, sorts, and displays employee data + some basic stats

employees = [
    {"id": 1, "name": "Alice", "age": 25, "department": "Engineering", "salary": 75000},
    {"id": 2, "name": "Bob", "age": 32, "department": "Marketing", "salary": 55000},
    {"id": 3, "name": "Charlie", "age": 29, "department": "Engineering", "salary": 85000},
    {"id": 4, "name": "David", "age": 41, "department": "HR", "salary": 60000},
    {"id": 5, "name": "Eva", "age": 27, "department": "Engineering", "salary": 70000}
]

valid_fields = ["name", "age", "salary"]


def get_filter_inputs():
    # asks the user what they want to filter by
    # keeps asking again if they type something that's not a number
    department = input("Enter department: ")

    while True:
        try:
            min_salary = int(input("Enter minimum salary: "))
            break
        except ValueError:
            print("Please enter a valid salary (numbers only).")

    while True:
        try:
            max_age = int(input("Enter maximum age: "))
            break
        except ValueError:
            print("Please enter a valid age (numbers only).")

    return department, min_salary, max_age


def filter_employees(employees, department, min_salary, max_age):
    """
    Goes through the employee list and only keeps the ones that match
    all 3 conditions - department, min salary, max age.
    """
    filtered = []

    for employee in employees:
        if employee["department"].lower() == department.lower() and employee["salary"] >= min_salary and employee["age"] <= max_age:
            filtered.append(employee)

    return filtered


def sort_employees(employees, sort_by):
    # sorts using a lambda so we can sort by whatever field the user picks
    return sorted(employees, key=lambda employee: employee[sort_by])


def display_employees(employees):
    # just prints everything out in a readable way instead of the ugly dict format
    if not employees:
        print("\nNo matching employees found.")
        return

    print("\nFiltered Employees")
    print("=" * 30)

    for employee in employees:
        print(f"ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Age: {employee['age']}")
        print(f"Salary: {employee['salary']}")
        print("-" * 30)


def show_statistics(employees):
    # basic stats - total count, average salary, highest/lowest paid person
    if not employees:
        print("\nNo employees to calculate stats for.")
        return

    total_employees = len(employees)
    average_salary = sum(employee["salary"] for employee in employees) / total_employees

    highest_salary_employee = max(employees, key=lambda employee: employee["salary"])
    lowest_salary_employee = min(employees, key=lambda employee: employee["salary"])

    print("\nEmployee Statistics")
    print("=" * 30)
    print(f"Total Employees: {total_employees}")
    print(f"Average Salary: {average_salary:.2f}")
    print(f"Highest Salary Employee: {highest_salary_employee['name']}")
    print(f"Lowest Salary Employee: {lowest_salary_employee['name']}")


def main():
    department, min_salary, max_age = get_filter_inputs()

    filtered_employees = filter_employees(employees, department, min_salary, max_age)

    # ask what to sort by, default to name if they type something wrong
    sort_by = input("Sort by (name/age/salary): ").lower()
    if sort_by not in valid_fields:
        print("Invalid sort field. Using 'name' by default.")
        sort_by = "name"

    filtered_employees = sort_employees(filtered_employees, sort_by)

    display_employees(filtered_employees)
    show_statistics(filtered_employees)


if __name__ == "__main__":
    main()