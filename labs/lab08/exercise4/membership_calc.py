base_membership_fee = 120
personal_training_fee = 80
locker_rental_fee = 25
towel_rental_fee = 15
one_time_joining_fee = 50

total_first_month_fee = (base_membership_fee + (personal_training_fee*6) + locker_rental_fee + towel_rental_fee + one_time_joining_fee)
print(f"The total first month fee is: {total_first_month_fee}")

monthly_fee_after_first_month = (base_membership_fee + (personal_training_fee*6) + locker_rental_fee + towel_rental_fee)
print(f"The monthly fee after the first month is: {monthly_fee_after_first_month}")

annual_fee = ((monthly_fee_after_first_month * 11)+ total_first_month_fee)
print(f"The annual fee is: {annual_fee}")