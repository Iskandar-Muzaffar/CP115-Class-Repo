#Iskandar Lab Test 3
#This code calculates the bill payment after applying discounts based on monthly usage.

monthly_usage = int(input("Enter Monthly Usage:")) #

discount = 0 # Initialize discount variable

# my code here

if monthly_usage >= 100:
    discount = 0.2
elif monthly_usage >= 50:
    discount = 0.05
else:
    discount = 0

bill_payment = monthly_usage * (1 - discount) # Calculate bill payment after discount

#print results
print(bill_payment)