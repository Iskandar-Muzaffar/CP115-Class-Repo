position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here

hourly_rate = 0

if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

overtime_rate = 0

overtime_rate = hourly_rate * 1.5

weekend_bonus = 0

if is_weekend == "Y":
    weekend_bonus = (overtime_hours * 5)
else:
    weekend_bonus = 0

overtime_pay = (overtime_hours * overtime_rate) + weekend_bonus
total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)