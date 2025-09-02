employee_name = input("Enter employee name: ")
base_salary = float(input("Enter base salary: "))
overtime_hours = int(input("Enter overtime hours worked:"))
tax_status = input("Enter tax status: ")

additional_deduction = 0.16

# TODO your code here
tax_rate = ""
if tax_status == "single" and base_salary >= 5000:
    tax_rate = 0.22
elif tax_status == "single" and base_salary < 5000:
    tax_rate = 0.18
elif tax_status == "married" and base_salary >= 6000:
    tax_rate = 0.20
elif tax_status == "married" and base_salary < 6000:
    tax_rate = 0.15
elif tax_status == "head" and base_salary >= 5500:
    tax_rate = 0.25
elif tax_status == "head" and base_salary < 5500:
    tax_rate = 0.19

net_salary = base_salary + (overtime_hours * 35) - (base_salary * tax_rate) - ( base_salary * additional_deduction )

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")