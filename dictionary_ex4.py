employees = {
    "E001": {"name": "Divya", "dept": "IT", "salary": 50000},
    "E002": {"name": "Rahul", "dept": "HR", "salary": 45000},
    "E003": {"name": "Priya", "dept": "IT", "salary": 55000}
}

# 1. Print all employee names
print("All Employees:")
for emp_id, details in employees.items():
    print(f"  {emp_id}: {details['name']}")

# 2. Print IT department employees
print("\nIT Department:")
for emp_id, details in employees.items():
    if details["dept"] == "IT":
        print(f"  {details['name']}")

# 3. Find average salary
total_salary = sum(emp["salary"] for emp in employees.values())
average_salary = total_salary / len(employees)
print(f"\nAverage Salary: ₹{average_salary}")
