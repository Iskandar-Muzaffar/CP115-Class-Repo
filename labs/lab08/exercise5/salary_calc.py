import employee_data

EPF = 0.11
SOCSO = 0.05
EIS = 0.02
deduction_rate = EPF + SOCSO + EIS 

medical_insurance = 50
parking = 30
fixed_deductions = medical_insurance + parking

overtime_pay = employee_data.overtime_hours * employee_data.overtime_rate
gross_salary = employee_data.basic_salary + overtime_pay
deductions = gross_salary * deduction_rate
net_salary = gross_salary - deductions - fixed_deductions
print(f"Gross Salary: RM{gross_salary}")
print(f"Deductions: RM{deductions}")
print(f"Fixed Deductions: RM{fixed_deductions}")
print(f"Net Salary: RM{net_salary}")