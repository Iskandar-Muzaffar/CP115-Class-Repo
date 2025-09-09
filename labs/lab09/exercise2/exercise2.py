employee_name = input("Enter employee name: ")
base_salary = int(input("Enter base salary: "))
overtime_hours = int(input("Enter overtime hours worked:"))
tax_status = input("Enter tax status: ")


epf_rate = 0.11
sosco_rate = 0.005
overtime_rate = 35

# TODO your code here
tax_rate = 0
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
 
net_salary = (base_salary + (overtime_hours * overtime_rate)) * (1 - tax_rate) * (1 - epf_rate - sosco_rate)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")