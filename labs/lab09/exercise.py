# if statement - always at the beginning
student_grade = 90

if student_grade >= 90:
    print("Excellent performance")
# elif positioning - can have multiple elif statements
student_grade = 85

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:    # After if
    print("Good performance") 
elif student_grade >= 70:    # After elif
    print("Satisfactory performance")
elif student_grade >= 60:    # After elif
    print("Minimum performance")

    # else positioning - always last
student_grade = 45

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:
    print("Good performance")
elif student_grade >= 70:
    print("Satisfactory performance") 
elif student_grade >= 60:
    print("Minimum performance")
else:                        # Always positioned last
    print("Below minimum performance")

    # Multiple independent health checks - use multiple if statements
weight = 59 # kg
height = 1.66  # meters
age = 18
exercise_hours = 2  # per week

bmi = weight / (height * height)

# Each check is independent - multiple can be True
if bmi >= 25:
    print("Recommendation: Consider weight management")
    
if age >= 40:
    print("Recommendation: Schedule regular health checkups")
    
if exercise_hours < 3:
    print("Recommendation: Increase physical activity")
    
if bmi < 18.5:
    print("Recommendation: Consider increasing caloric intake")

    # BMI classification - use if-elif-else chain
weight = 85  # kg  
height = 1.75  # meters
bmi = weight / (height * height)

print(f"BMI: {bmi:.1f}")

# Only one classification should apply
if bmi >= 30:
    print("BMI Category: Obese")
elif bmi >= 25:
    print("BMI Category: Overweight")  
elif bmi >= 18.5:
    print("BMI Category: Normal weight")
else:
    print("BMI Category: Underweight")

    # Correct: Most specific conditions first
score = 95

if score == 100:
    print("Perfect score!")
elif score >= 90:  
    print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("Below B grade")