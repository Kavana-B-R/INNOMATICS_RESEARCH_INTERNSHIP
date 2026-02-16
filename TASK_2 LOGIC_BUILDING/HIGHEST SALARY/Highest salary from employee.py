employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}

highest_employee = max(employees, key=employees.get)
highest_salary = employees[highest_employee]

print("Highest Salary:", highest_employee, "-", highest_salary)
